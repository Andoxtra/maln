# Mensch ärgere Licht nicht (MALN)

A digital version of the classic German board game **"Mensch ärgere dich nicht"**
(similar to Ludo / Parcheesi). The board is a 3D-printed case with **144 RGB LEDs**,
driven by a **Raspberry Pi**. Each of the up to 4 players has a controller with
**two buttons** and a small **OLED display**.

For development without the hardware, the game can also run on a PC:
the board is shown in a **Tkinter window** and players use the **keyboard and console**.

The full project documentation (in German) is in
[docs/Projektdokumentation.pdf](docs/Projektdokumentation.pdf).

---

## Repository layout

```
maln/
├── main.py              ▶ Start the game here
├── RunInThreads.py      Runs game logic and display in parallel
├── helper.py            Shared helper functions (colors, field calculations)
├── requirements.txt     Python dependencies
├── Game/                Game logic (rules, players, figures, dice, input/output devices)
├── GUI/                 Display of the board
│   ├── Virtuell/        Tkinter window (PC)
│   └── Physical/        LED board (Raspberry Pi)
├── docs/                Documentation
│   ├── ARCHITECTURE.md      ★ How the code works – read this before changing code
│   ├── Spielanleitung.docx  Game rules (German)
│   ├── Projektdokumentation.pdf  Full project documentation (German)
│   ├── images/              Class diagram and flow chart
│   └── reference/           Color codes and field coordinates
├── hardware/            Everything needed to build the physical board
│   ├── 3d-print/            STL files for all printed parts (+ Tinkercad link)
│   ├── BUILD.md             ★ Step-by-step build guide
│   ├── schematics/          Board + controller wiring diagrams, Fritzing sources (fritzing/)
│   ├── pcb/                 Circuit boards: Gerber files, schematics (PDF), 3D models (STEP), BOM
│   └── SpielbrettInfoMADN.xlsx  Field / LED layout of the board
└── deploy/
    └── madn.service     systemd service to autostart the game on the Raspberry Pi
```

---

## Quick start (PC, no hardware)

Requirements: Python 3 and Git.

```bash
# 1. Clone the repository
git clone git@github.com:Andoxtra/maln.git
cd maln

# 2. Create and activate a virtual environment
python -m venv .venv
source .venv/bin/activate        # Linux / macOS
.\.venv\Scripts\activate         # Windows

# 3. Install dependencies
pip install -r requirements.txt

# 4. Start the game
python main.py
```

The board opens in a separate window. All interaction happens in the **console**:

| Key     | Action                                                  |
|---------|---------------------------------------------------------|
| `d`     | **Next** – change selection (number of players / figure) |
| `Enter` | **Confirm** – confirm selection / roll the dice          |

> **Tips**
> - On Windows, use **Windows + Arrow keys** to place the console and the board window side by side.
> - On Linux, the `keyboard` package may need root rights (`sudo`) to read key presses.

---

## Configuration

There are two places to switch between PC mode and hardware mode:

### 1. Board display – `main.py`

```python
runner = RunInThreads(tkinterGUI)    # Tkinter window on the PC (default)
runner = RunInThreads(physicalGUI)   # LED board on the Raspberry Pi
```

### 2. Player input/output – `Game/GameField/Player/config/playerConfig.py`

```python
input_type  = "Keyboard"    # or "Physical"   (buttons on the controllers)
output_type = "Console"     # or "LCDDisplay" (OLED displays on the controllers)
```

> **Important:** `physicalGUI`, `"Physical"` and `"LCDDisplay"` only work on the
> Raspberry Pi with the real board and controllers connected.
> I²C addresses of the controllers are set in
> `Game/GameField/Player/IO/config/physicalAddressConfig.py`.

---

## How to play

Full rules (German): [docs/Spielanleitung.docx](docs/Spielanleitung.docx)

**Goal:** Be the first player to bring all 4 figures from the start fields around the
board and into your goal fields.

**Setup:** The **yellow** player chooses the number of players (2 or 4) with the
*Next* button (right button / `d`) and confirms with the *Enter* button (left button / `Enter`).
Then every player rolls once – the highest roll starts.

**Turn:**
1. Roll the dice with *Enter*.
2. If more than one figure can move, choose one with *Next* and confirm with *Enter*.
   The selected figure blinks and its target field lights up white.
3. A 6 lets you roll again. You need a 6 to bring a figure onto the board.
   Landing on an opponent's figure sends it back to its start field.

**House rules used:**
- **Three rolls:** If you have no figure on the track (all on start fields, or the ones in
  the goal cannot move further), you may roll up to three times to get a 6.
- **Two players:** Yellow plays against red.

---

## Running on the Raspberry Pi

1. Clone the repository to `/root/game` and create the virtual environment in `/root/game/.venv`
   (these paths are hard-coded in `deploy/madn.service` – adjust the file if you use different paths).
2. Install dependencies: `pip install -r requirements.txt`
3. Set `physicalGUI` in `main.py` and `"Physical"` / `"LCDDisplay"` in `playerConfig.py`.
4. Install the autostart service:
   ```bash
   sudo cp deploy/madn.service /etc/systemd/system/
   sudo systemctl daemon-reload
   sudo systemctl enable --now madn.service
   ```

---

## Building the hardware

**Step-by-step guide: [hardware/BUILD.md](hardware/BUILD.md)** (parts list, printing, PCBs, wiring, Pi setup).

- **3D-printed parts:** [hardware/3d-print/](hardware/3d-print/). The file names say how many
  of each part to print and in which color, e.g. `72x Transparent - Light-Inner.stl`.
  The original model is on Tinkercad (link file in the same folder).
- **Controller wiring:** [hardware/schematics/](hardware/schematics/) – one wiring diagram per controller
  (`controller00`, `01`, `10`, `11`).
  The editable Fritzing sources (`.fzz`) are in [hardware/schematics/fritzing/](hardware/schematics/fritzing/).
- **Circuit boards:** [hardware/pcb/](hardware/pcb/) – three boards designed in EasyEDA and
  manufactured by JLCPCB. Each folder contains the Gerber ZIP (send this to the manufacturer),
  the schematic as PDF and a 3D model (`.step`):
  - `RGB-Platine/` – LED board (also has the bill of materials and pick-and-place file for assembly)
  - `Kurzes-Verbindungsstueck/` – short connector board
  - `Langes-Verbindungsstueck/` – long connector board
- **Board / LED layout:** [hardware/SpielbrettInfoMADN.xlsx](hardware/SpielbrettInfoMADN.xlsx)
- More details (wiring of the prototype, parts list, schematics) are in the
  [project documentation](docs/Projektdokumentation.pdf).

---

## For developers

Start with [docs/ARCHITECTURE.md](docs/ARCHITECTURE.md). It explains the module structure,
the threading model, the input/output abstraction and how the 144 board fields are numbered.

## License

See [LICENSE](LICENSE).
