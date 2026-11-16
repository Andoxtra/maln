# Architecture

This document explains how the code is structured and how the game state is represented.
For setup and usage, see the main [README](../README.md).

Diagrams:
- Class diagram: [images/Klassendiagramm.png](images/Klassendiagramm.png)
- Program flow chart: [images/Flussdiagramm.png](images/Flussdiagramm.png)

---

## 1. Module overview

```
main.py                     Entry point – picks the GUI and restarts the game in an endless loop
RunInThreads.py             Runs game logic and GUI in parallel (game in a thread, GUI in main thread)
helper.py                   Shared helpers: color codes → hex/RGB, start-field calculation, list utils

GUI/                        "Renderers" – they only DRAW the current play field
├── Virtuell/GuiTkinter.py  Draws the board in a 920×920 Tkinter window (for development on a PC)
└── Physical/GuiPhysical.py Drives the 144 NeoPixel LEDs of the real game board (Raspberry Pi, SPI)

Game/                       Game logic
├── Game.py                 Game flow: number of players, play order, turn loop, win animation
└── GameField/
    ├── GameField.py        The board: holds all players, computes the play-field color list,
    │                       figure selection, moving and beating figures
    └── Player/
        ├── Player.py       One player: 4 figures, dice, controller; computes possible moves
        ├── Figure/Figure.py   State and position of a single game piece
        ├── Dice/Dice.py       Random number 1–6
        ├── Phelper/playerHelper.py  Helper functions for Player
        ├── config/playerConfig.py   ★ Choose input/output type per player
        └── IO/
            ├── Controller.py         Creates the input + output object for one player
            ├── config/physicalAddressConfig.py  I²C bus / addresses per controller
            ├── Input/
            │   ├── Virtuell/Keyboard.py         Keyboard input (d = Next, Enter = Enter)
            │   └── Physical/PortExpander.py     MCP23008 port expander with 2 buttons
            │       Physical/PhysicalButton.py   One push button on the port expander
            └── Output/
                ├── Virtuell/Console.py          Prints dice, selection etc. to the console
                └── Physical/Display.py          Draws the same info on a 128×64 SSD1306 OLED
                    Physical/helper/displayHelper.py  Pixel graphics (digits, dice, figures)
```

## 2. How the program runs

1. `main.py` creates a `RunInThreads` object with either `"Tkinter"` or `"Physical"`.
2. `RunInThreads.run_game()`:
   1. `Game.initialize_game()` – the **first player (yellow)** chooses 2 or 4 players,
      then every player rolls once; the highest roll starts.
   2. The selected GUI is created.
   3. `Game.start_game()` is started in a **separate thread** (the game loop).
   4. The GUI's `render_gui()` runs in the main thread and redraws every 300 ms by
      reading `game.game_field.play_field`.
3. When a player wins, a win animation is shown, `game.running` becomes `False`,
   the GUI stops, and `main.py` starts a new game.

The game logic and the GUI only share **one thing**: the list `GameField.play_field`.
The logic writes color codes into it, the GUI reads and draws it.

## 3. Input / output abstraction

Every player has a `Controller` with one **input** and one **output** object.
All input classes provide `get_input()` / `wait_for_input_action()` and return
`"Next"` or `"Enter"`. All output classes provide the same `show_*` / `clear_*` methods.
This is why the game logic does not care whether it runs on a PC or on the real board.

| Setting in `playerConfig.py` | Value          | Class used                    |
|------------------------------|----------------|-------------------------------|
| `input_type`                 | `"Keyboard"`   | `Keyboard` (keys `d`, `Enter`) |
| `input_type`                 | `"Physical"`   | `PortExpander` (right button = Next, left button = Enter) |
| `output_type`                | `"Console"`    | `Console`                     |
| `output_type`                | `"LCDDisplay"` | `Display` (SSD1306 OLED)      |

The hardware addresses for the physical controllers (I²C bus pins, display and
port-expander addresses) are in `Game/GameField/Player/IO/config/physicalAddressConfig.py`.

## 4. Player colors

| Color index | Player |
|-------------|--------|
| 0           | Yellow |
| 1           | Green  |
| 2           | Red    |
| 3           | Blue   |

In a 2-player game, green (1) and blue (3) are removed, so yellow plays against red.

## 5. The play field (index map)

`GameField.play_field` is a list of **144 color codes**:

| Index     | Meaning |
|-----------|---------|
| 0 – 15    | Start fields ("B" fields), 4 per color: color `c` uses `c*4 … c*4+3` |
| 16 – 31   | Goal fields ("home"), 4 per color: color `c` uses `c*4+16 … c*4+19` |
| 32 – 71   | The 40-field track. Color `c` enters the track at `c*10 + 32` (see `helper.get_start_field_by_color`). Moving past 71 wraps around (−40). |
| 72 – 143  | Second LED layer (background / highlight). Same layout as 0–71, shifted by +72. Used to make the selected figure blink and to mark the target field in white. |

`GuiTkinter.py` and `GuiPhysical.py` each contain a lookup table that maps these
logical indices to window coordinates or to the position in the LED chain.
The spreadsheet [`hardware/SpielbrettInfoMADN.xlsx`](../hardware/SpielbrettInfoMADN.xlsx)
documents the front/background fields of the physical board.

### Figure state (`Figure.py`)

| Attribute      | Values |
|----------------|--------|
| `status`       | `0` = on start field, `1` = on track, `2` = in goal |
| `position`     | Index in the play field (`-1` = not yet placed) |
| `fields_to_go` | Remaining track fields before the goal (starts at 39) |

## 6. Color codes

The values in `play_field` are color codes, translated to RGB in `helper.get_color_map()`.
Also listed in [reference/colorSchema.txt](reference/colorSchema.txt).

| Code | Color        | Code | Color        | Code | Color        |
|------|--------------|------|--------------|------|--------------|
| 0    | yellow       | 5    | half green   | 10   | black (off)  |
| 1    | green        | 6    | half red     | 11   | blink yellow |
| 2    | red          | 7    | half blue    | 12   | blink green  |
| 3    | blue         | 8    | half white   | 13   | blink red    |
| 4    | half yellow  | 9    | white        | 14   | blink blue   |

"Half" colors are dimmed versions used for empty fields; codes 11–14 make an LED blink.

## 7. Reference files

- [reference/colorSchema.txt](reference/colorSchema.txt) – color-code list (same as the table above)
- [reference/playFieldInfo.txt](reference/playFieldInfo.txt) – pixel coordinates of each field in the
  Tkinter window (`[x1, y1, x2, y2, value]`; the 5th value marks the owning color, 4 = neutral).
  It is an earlier copy of the `map_config_list` in `GUI/Virtuell/GuiTkinter.py` and is kept for
  reference only – the code does **not** load this file; the live table is in `GuiTkinter.py`.
