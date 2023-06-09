echo 'Installing Homebrew';
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)";

echo 'Adding Homebrew to PATH';
(echo; echo 'eval "$(/opt/homebrew/bin/brew shellenv)"') >> /Users/mathiscote/.zprofile
    eval "$(/opt/homebrew/bin/brew shellenv)";

echo 'Bootstraping dependencies:';
echo 'Installing Python';
brew install python;

echo 'Installing wget';
brew install wget

echo 'Downloading python install script from Github'
mkdir ~/temp/
cd ~/temp/
wget https://raw.githubusercontent.com/BenocxX/macos/main/install.py