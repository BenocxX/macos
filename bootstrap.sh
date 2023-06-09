echo 'Installing Homebrew';
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)";

echo 'Adding Homebrew to PAHT';
(echo; echo 'eval "$(/opt/homebrew/bin/brew shellenv)"') >> /Users/mathiscote/.zprofile
    eval "$(/opt/homebrew/bin/brew shellenv)";

echo 'Installing Python';
brew install python;

echo 'Installing wget';
brew install wget

echo 'Downloading python install script from Github'
mkdir ~/temp/
cd ~/temp/
wget https://raw.githubusercontent.com/BenocxX/scripts/main/macos/install.py?token=GHSAT0AAAAAACDXERC6D3EJBRHZQ24E5GXIZEDRELQ