# Ideas for Future Improvements

Collected ideas to make MALN **cheaper and easier to rebuild**. Nothing here is implemented yet.

Cost basis: the parts list in the [project documentation](Projektdokumentation.pdf) (appendix 3),
total about **€414**.

| Cost block | Actual cost | Share |
|------------|-------------|-------|
| Custom PCBs (LED boards, connector boards, JLCPCB shipping) | ≈ €183 | ≈ 44 % |
| Raspberry Pi 5, power supply, fan, SD card, port extensions | ≈ €102 | ≈ 25 % |
| Everything else (filament, displays, port expanders, mirrors, …) | rest | |

---

## Idea 1: Replace the Raspberry Pi with an ESP32 (C++ port)

Replace the Raspberry Pi 5 with an **ESP32-WROOM-32D** (a few euros) and port the code to C++.
The ESP32 covers everything the board needs.

### Hardware fit

| Today (Pi + Python) | ESP32 + C++ | |
|---------------------|-------------|---|
| 144 WS2812 LEDs via `neopixel_spi` | RMT peripheral with **FastLED** or **Adafruit_NeoPixel** | ✅ |
| **Two I²C buses** (GPIO0/1 and GPIO2/3) | ESP32 has exactly **two hardware I²C controllers** (`Wire`, `Wire1`), usable on any pins | ✅ |
| 4× SSD1306 OLED (128×64) | **Adafruit_SSD1306** or **U8g2** (1 KB frame buffer each) | ✅ |
| 4× MCP23008 port expander | **Adafruit_MCP23X08** (in the Adafruit MCP23017 library) | ✅ |
| Python `random` for the dice | `esp_random()` (hardware random number generator) | ✅ |

The two I²C buses are needed because an SSD1306 only has two addresses (0x3C/0x3D),
so at most two displays fit on one bus.

### Why the code ports well

- About **1,000 lines** of game logic and display code to port (Tkinter GUI and keyboard input are not needed).
- The input/output classes (`Keyboard`/`PortExpander`, `Console`/`Display`) already share one interface.
  In C++ they become abstract `Input` / `Output` classes with virtual methods.
- The whole game state is `play_field`, which becomes `uint8_t playField[144]`.
- Lookup tables (`get_index_from_map()` in `GuiPhysical.py`, the color map in `helper.py`) become `const` arrays.
- `displayHelper.py` only uses simple drawing calls (`draw.line`, `draw.point`). These map almost directly to
  Adafruit GFX (`drawLine`, `drawPixel`).

### Things to watch out for

1. **Watchdog:** `wait_for_input_action()` and `is_one_button_pressed_and_released()` spin in `while True`
   loops. On the ESP32, add `delay(10)` / `vTaskDelay()` inside them. This also debounces the buttons.
2. **Threading:** `RunInThreads` runs the game logic and the LED refresh in parallel. Use two FreeRTOS tasks
   (one per core). For blinking, use a `bool blinkOn` that flips on each refresh instead of reading the LED
   color back like `GuiPhysical` does.
3. **2-player mode:** `set_number_of_players()` removes players from the list with `pop()`. In C++, keep
   4 players with an `active` flag instead, to avoid index bugs.
4. **Pins on the WROOM-32D:**
   - Don't use GPIO6–11 (flash memory) or the boot-mode pins 0, 2, 12 and 15.
   - GPIO34–39 are input-only.
   - Suggested: I²C bus 0 on GPIO21/22, I²C bus 1 on GPIO25/26, LED data on GPIO18.
5. **Voltage levels:** the ESP32 uses 3.3 V logic, like the Pi.
   - A level shifter (e.g. 74AHCT125) makes the WS2812 data signal more reliable.
   - The ESP32 pins don't tolerate 5 V, so make sure the I²C pull-ups go to 3.3 V.

### Trade-offs

- **Gained:** much cheaper, boots in under a second, low power use, no SD card that can get corrupted.
- **Lost:** PC mode (Tkinter window and keyboard play). Keep the Python version as a simulator for testing
  the game logic. Updates over SSH/git are replaced by USB flashing or OTA updates over WiFi.
- **Case:** the Pi mount, port extensions (HDMI, Ethernet, USB) and the status-LED cover
  (`LED-Abdeckung-PWR-und-ACT`) would need to be adapted.

### Suggested porting order

Use PlatformIO with the Arduino framework.

1. **LEDs only:** show the start layout using the `ledIndex` table, which checks the board wiring.
2. **One controller** (MCP23008 + OLED), then all four on both buses.
3. **Game logic:** `Figure` → `Player` → `GameField` → `Game`.
4. **Display graphics** from `displayHelper.py`.

---

## Idea 2: Reduce the cost of the custom PCBs

Most of the PCB cost comes from the **assembled LED boards** (€140 of ≈ €183), not the connector boards.

### Option A: Optimize the current design (little redesign)

- **Drop the through-hole connectors.** Each LED board has 4 (PZ200, H1–H4), so 288 in total plus
  through-hole assembly. Use plain solder pads and solder the connector boards or wires directly.
- **Replace the 0 Ω "bridge" (R1) with a solder jumper.** The connector boards then need no assembly,
  and one design per length is enough.
- **Panelize:** put several small boards on one panel and break them apart after delivery.
- **Check the parts category:** at JLCPCB, "Extended" parts cost a setup fee per part type.
  Look for "Basic" alternatives.

### Option B: One PCB per quarter (recommended)

The case is already split into **4 quarters with 18 fields each**. One PCB per quarter carries all
36 LEDs, with the connections between fields on the board.

- Replaces **72 LED boards and 121 connector boards with 4 boards**. Only the 4 quarter-to-quarter
  links remain as wires.
- **Far less soldering and wiring.** The original LED strip plan was dropped because of about 864 solder joints.
- The field layout is rotationally symmetric, so **one design × 4** may be enough, as long as the data
  input and output are in the right place.
- Fully assembled by JLCPCB, with only 2 SMD part types.
- **Caveats:**
  - Prices jump for boards larger than 100×100 mm, so get a quote for the quarter size.
  - LED positions must match the light tubes in the case (check with the `.step` models and Tinkercad).
  - The LED order changes, so the `ledIndex` table must be updated.

### Option C: No custom PCBs (cheapest, most labor)

- **Cut-up WS2812B LED strip:** a 144-LED strip cost **€10.99** (it's on the original parts list).
  This needs a lot of soldering.
- **Ready-made LED modules:** small round WS2812B boards (packs of 100), or pre-wired pixel strings.
  Less soldering, but the spacing between fields isn't regular, so cable lengths must be adapted.

### Option D: One LED per field (combine with any option)

Each field currently has **2 LEDs**: front plus a background layer for highlighting (play-field indices 72–143).
With 1 LED per field:

- Half the LEDs (72 instead of 144), simpler boards, less current.
- **Trade-off:** no separate highlight layer. The selected figure and its target field would blink on the
  same LED, which needs a code change in `GameField` / `Game`.

### Comparison

| Option | PCB cost | Effort | Easy to rebuild |
|--------|----------|--------|-----------------|
| Current design | ≈ €183 | high (wiring) | medium |
| A: Optimized current design | lower | high (wiring) | medium |
| B: One PCB per quarter | low–medium | low | **high** |
| C: LED strip / modules | **≈ €15–30** | **very high** | low |
| D: 1 LED per field | halves the LEDs | – | – |

---

## Recommended combination

**ESP32 (Idea 1) + one PCB per quarter (Idea 2, Option B).** This removes both big cost blocks
(Raspberry Pi and the many small PCBs) and most of the wiring work, which makes the board practical
for others to rebuild.
