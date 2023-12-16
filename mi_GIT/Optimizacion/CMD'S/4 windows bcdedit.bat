@echo
start https://www.instagram.com/yostrength_/

bcdedit /set disabledynamictick yes
bcdedit /set useplatformtick Yes
bcdedit /set quietboot yes
bcdedit /set bootux disabled
bcdedit /set bootmenupolicy legacy
bcdedit /set {globalsettings} custom:16000067 true
bcdedit /set {globalsettings} custom:16000069 true
bcdedit /set {globalsettings} custom:16000068 true

pause