# Omarchy Circadian

Light/dark theme pairs based on sunrise and sunset. A systemd user timer runs a short Qt/C++ process every five minutes; nothing runs continuously. The solar calculation handles polar day and night. Theme transitions can be delayed by up to about six minutes (and until login/wake if the computer was asleep).

## Install

Requires Omarchy, a C++17 compiler, make, pkg-config, Qt 6 Core and Network development libraries, and systemd user services. Run `./install`, then set your location:

```sh
circadian location auto                       # approximate IP geolocation
circadian location search 'Portland, Oregon, USA'  # city or postal code plus country
circadian location coords 45.52 -122.68      # latitude longitude
circadian check
```

Automatic lookup sends your IP to ipapi.co. Search sends your query and IP to OpenStreetMap Nominatim; ambiguous results are printed rather than chosen. Coordinates require no network. The result is stored in `~/.config/omarchy-circadian/config.json`; scheduled checks make no network requests. Check provider policies before use.

## Pairs

```sh
circadian list
circadian next                  # cycle and apply
circadian select catppuccin
circadian select solarized
circadian pair my-pair light-theme-name dark-theme-name
circadian select my-pair
circadian status
```

The Solarized pair requires themes installed under the names `solarized` and `solarized-light`. For example, use `omarchy theme install https://github.com/Gazler/omarchy-solarized-theme` and `omarchy theme install https://github.com/dfrico/omarchy-solarized-light-theme`. Omarchy's installer applies each theme and replaces any existing user theme with the same name. Review those third-party repositories first.

The timer enforces the chosen pair, so a manually selected unrelated theme is replaced at the next check. Set another pair or stop the timer to pause automation.

## Uninstall

```sh
systemctl --user disable --now omarchy-circadian.timer
rm ~/.config/systemd/user/omarchy-circadian.{timer,service} ~/.local/bin/circadian
systemctl --user daemon-reload
```

Your configuration and separately installed themes are retained. Remove `~/.config/omarchy-circadian` manually if desired.
