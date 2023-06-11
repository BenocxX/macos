import os

OH_MY_ZSH = 'https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh'
ZSHRC = 'https://gist.githubusercontent.com/BenocxX/02c64b944e2ade276dc1c5faa09d113a/raw/bfebd172ac00b419d32ea3582571d3af8a3d001d/.zshrc'
ZSH_AUTOSUGGESTIONS = 'https://github.com/zsh-users/zsh-autosuggestions'
ZSH_SYNTAX_HIGHLIGHTING = 'https://github.com/zsh-users/zsh-syntax-highlighting.git'
VSCODE_SETTINGS = 'https://gist.githubusercontent.com/BenocxX/df7eeea87e8db5d52544ec646ef18ec5/raw/691af7e60f529be8c2ef4fe16f76f7800e5c5859/settings.json'
VSCODE_KEYBINDS = 'https://gist.githubusercontent.com/BenocxX/a7729cf68af081d114e6e22e93221fe7/raw/3450d8c44211994f99e48216740bac29d894a789/keybindings.json'
IDEAVIMRC = 'https://gist.githubusercontent.com/BenocxX/c344f6493bb544ab0218a4cc006b16f9/raw/c51716602754aad9e3f648d4dadccb2e3d807e50/.ideavimrc'

def dark_mode():
    print('============== Set dark mode ==============')
    os.system(f'osascript -e \'tell app "System Events" to tell appearance preferences to set dark mode to not dark mode\'')

def accent_menu():
    print('============== Disable Accent Menu ==============')
    os.system('defaults write -g ApplePressAndHoldEnabled -bool false')

def dock():
    print('============== Config Dock ==============')
    dock_options = [
        'show-recents -bool false',
        'persistent-apps -array',
        'tilesize -integer 48',
    ]

    for option in dock_options:
        os.system(f'defaults write com.apple.dock {option}')

    os.system('osascript -e \'tell application "System Events" to set the autohide of the dock preferences to true\'')

    os.system('killall Dock')

def trackpad():
    print('============== Config Trackpad ==============')
    trackpad_options = [
        'Clicking -bool true'
    ]

    trackpad_devices = [
        'com.apple.driver.AppleBluetoothMultitouch.trackpad',
        'com.apple.AppleMultitouchTrackpad'
    ]
    
    for device in trackpad_devices:
        for option in trackpad_options:
            os.system(f'defaults write {device} {option}')

def homebrew():
    print('============== Homebrew installations ==============')
    cli_apps = [
        'fzf',
        'docker',
        'docker-compose',
        'node'
    ]

    for app in cli_apps:
        os.system(f'brew install {app}')

    casks_apps = [
        'firefox',
        'visual-studio-code',
        'fork',
        'discord',
        'figma',
        'iterm2',
        'docker',
        'dotnet-sdk'
    ]

    for app in casks_apps:
        os.system(f'brew install --cask {app}')

def iterm():
    print('============== Iterm ==============')

    os.system(f'sh -c "$(wget {OH_MY_ZSH} -O -)"')
    os.system(f'wget {ZSHRC} -O ~/.zshrc')

    # zsh plugins
    os.system(f'git clone {ZSH_AUTOSUGGESTIONS} ~/.oh-my-zsh/custom/plugins/zsh-autosuggestions')
    os.system(f'git clone {ZSH_SYNTAX_HIGHLIGHTING} ~/.oh-my-zsh/custom/plugins/zsh-syntax-highlighting')

def vscode():
    print('============== Config VSCode ==============')

    vscode_extensions = [
        'ms-python.python',
        'akamud.vscode-theme-onedark',
        'akamud.vscode-theme-onelight',
        'mikestead.dotenv',
        'dbaeumer.vscode-eslint',
        'github.copilot',
        'ecmel.vscode-html-css',
        'moalamri.inline-fold',
        'yzhang.markdown-all-in-one',
        'pkief.material-icon-theme',
        'ms-playwright.playwrigh',
        'esbenp.prettier-vscode',
        'prisma.prisma',
        'python.vscode-pylance',
        'fivethree.vscode-svelte-snippets',
        'svelte.svelte-vscode',
        'ardenivanov.svelte-intellisense',
        'bradlc.vscode-tailwindcss',
        'gruntfuggly.todo-tree',
        'vscodevim.vim'
    ]

    for extension in vscode_extensions:
        os.system(f'code --install-extension {extension}')

    # Gets settings.json and keybindings.json from gist
    os.system(f'wget {VSCODE_SETTINGS} -O ~/Library/Application\ Support/Code/User/settings.json')
    os.system(f'wget {VSCODE_KEYBINDS} -O ~/Library/Application\ Support/Code/User/keybindings.json')

def pin_to_dock():
    print('============== Pin apps to Dock ==============')
    apps = [
        '/Applications/Firefox.app',
        '/Applications/Visual Studio Code.app'
    ]

    for app in apps:
        os.system(f'defaults write com.apple.dock persistent-apps -array-add "<dict><key>tile-data</key><dict><key>file-data</key><dict><key>_CFURLString</key><string>{app}</string><key>_CFURLStringType</key><integer>0</integer></dict></dict></dict>"')

    os.system('killall Dock')

def jetbrains():
    print('============== Config Jetbrains ==============')
    os.system(f'wget {IDEAVIMRC} -O ~/.ideavimrc')

print('============== Start ==============')
dark_mode()
accent_menu()
dock()
trackpad()
homebrew()
iterm()
vscode()
pin_to_dock()
jetbrains()
print('============== End ==============')
