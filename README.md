# macos
Scripts to configure MacOS

## Install bootstraping script
```bash
https://github.com/BenocxX/macos/blob/main/bootstrap.sh
```

---

# Other

## MacOS config
Dark mode:
```bash
osascript -e 'tell app "System Events" to tell appearance preferences to set dark mode to not dark mode'
```

Dock:
```bash
defaults write com.apple.dock show-recents -bool false;
defaults write com.apple.dock persistent-apps -array;
killall Dock;
osascript -e 'tell application "System Events" to set the autohide of the dock preferences to true';
```

## Homebrew
First, install homebrew:
```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

Them add it to path:
```bash
(echo; echo 'eval "$(/opt/homebrew/bin/brew shellenv)"') >> /Users/mathiscote/.zprofile
    eval "$(/opt/homebrew/bin/brew shellenv)"
```

### Install cli tools and casks
```bash
brew install --cask firefox
brew install --cask visual-studio-code
```

### Add to docks
```bash
# Firefox
defaults write com.apple.dock persistent-apps -array-add "<dict><key>tile-data</key><dict><key>file-data</key><dict><key>_CFURLString</key><string>/Applications/Firefox.app</string><key>_CFURLStringType</key><integer>0</integer></dict></dict></dict>";

# Visual Studio Code
defaults write com.apple.dock persistent-apps -array-add "<dict><key>tile-data</key><dict><key>file-data</key><dict><key>_CFURLString</key><string>/Applications/Visual Studio Code.app/</string><key>_CFURLStringType</key><integer>0</integer></dict></dict></dict>";

# Save
killall cfprefsd; 
killall Dock;
```

## Firefox
Add extensions:
- Dashlane
- UBlock Origins
- Sponsorblock

## Visual Studio Code
```bash
code --install-extension ms-python.python
```