; Script generated by the Inno Setup Script Wizard.
; SEE THE DOCUMENTATION FOR DETAILS ON CREATING INNO SETUP SCRIPT FILES!


;#define Debug
#define B3_VERSION_NUMBER "1.6.0"
#define B3_VERSION_SUFFIX "b2"

[Setup]
; NOTE: The value of AppId uniquely identifies this application.
; Do not use the same AppId value in installers for other applications.
; (To generate a new GUID, click Tools | Generate GUID inside the IDE.)
;AppId={{F04D6FC4-CF46-4409-995A-04BEB0B219E6}
AppId=5FB180C6-A3B3-46CF-85E0-F00168F1569C
AppName=BigBrotherBot
AppVerName=BigBrotherBot {#B3_VERSION_NUMBER}{#B3_VERSION_SUFFIX}
AppPublisher=BigBrotherBot
AppPublisherURL=http://www.bigbrotherbot.net/
AppSupportURL=http://www.bigbrotherbot.net/
AppUpdatesURL=http://www.bigbrotherbot.net/
DefaultDirName={pf}\BigBrotherBot_{#B3_VERSION_NUMBER}{#B3_VERSION_SUFFIX}
DefaultGroupName=BigBrotherBot
LicenseFile=gpl-2.0.txt
OutputBaseFilename=BigBrotherBot-{#B3_VERSION_NUMBER}{#B3_VERSION_SUFFIX}
Compression=lzma/ultra64
SolidCompression=true
InternalCompressLevel=normal
DisableStartupPrompt=true
SetupLogging=true
VersionInfoVersion=1.0
VersionInfoDescription=B3 installation
VersionInfoCopyright=www.bigbrotherbot.net
AppCopyright=
VersionInfoTextVersion=1.0
VersionInfoProductName=BigBrotherBot
VersionInfoProductVersion={#B3_VERSION_NUMBER}
ExtraDiskSpaceRequired=11790316
RestartIfNeededByRun=false
PrivilegesRequired=none
WizardImageBackColor=clBlack
WindowVisible=false
BackColor=clBlack
BackColor2=clYellow
WizardSmallImageFile=WizB3SmallImage.bmp
WizardImageFile=WizB3Image.bmp
UsePreviousAppDir=false

[Languages]
Name: english; MessagesFile: compiler:Default.isl
Name: basque; MessagesFile: compiler:Languages\Basque.isl
Name: brazilianportuguese; MessagesFile: compiler:Languages\BrazilianPortuguese.isl
Name: catalan; MessagesFile: compiler:Languages\Catalan.isl
Name: czech; MessagesFile: compiler:Languages\Czech.isl
Name: danish; MessagesFile: compiler:Languages\Danish.isl
Name: dutch; MessagesFile: compiler:Languages\Dutch.isl
Name: finnish; MessagesFile: compiler:Languages\Finnish.isl
Name: french; MessagesFile: compiler:Languages\French.isl
Name: german; MessagesFile: compiler:Languages\German.isl
Name: hebrew; MessagesFile: compiler:Languages\Hebrew.isl
Name: hungarian; MessagesFile: compiler:Languages\Hungarian.isl
Name: italian; MessagesFile: compiler:Languages\Italian.isl
Name: norwegian; MessagesFile: compiler:Languages\Norwegian.isl
Name: polish; MessagesFile: compiler:Languages\Polish.isl
Name: portuguese; MessagesFile: compiler:Languages\Portuguese.isl
Name: russian; MessagesFile: compiler:Languages\Russian.isl
Name: slovak; MessagesFile: compiler:Languages\Slovak.isl
Name: slovenian; MessagesFile: compiler:Languages\Slovenian.isl
Name: spanish; MessagesFile: compiler:Languages\Spanish.isl

[Icons]
Name: {group}\{cm:executable,b3_run}; Filename: {app}\b3_run.exe; Parameters: "--config ""{commonappdata}\BigBrotherBot\conf\b3.xml"""; WorkingDir: {app}; Flags: dontcloseonexit; IconFilename: {app}\b3.ico; Comment: Run BigBrotherBot {#B3_VERSION_NUMBER}{#B3_VERSION_SUFFIX}; IconIndex: 0
Name: {group}\{cm:configWizard,Config wizard}; Filename: {app}\b3_run.exe; Parameters: "--config ""{commonappdata}\BigBrotherBot\conf\b3.xml"" --setup"; WorkingDir: {app}; Comment: Run the B3 setup wizard; Flags: dontcloseonexit
Name: {group}\{cm:B3ConfDir,config}; Filename: {commonappdata}\BigBrotherBot\
Name: {group}\{cm:extplugins,extplugins}; Filename: {app}\extplugins\; IconFilename: {app}\b3-plugins-icon.ico; IconIndex: 0
Name: {group}\extra\{cm:docs,docs}; Filename: {app}\docs\
Name: {group}\extra\{cm:sql,sql}; Filename: {app}\sql\
Name: {group}\{cm:UninstallProgram,BigBrotherBot}; Filename: {uninstallexe}
Name: {group}\web\{cm:Website,BigBrotherBot}; Filename: http://www.bigbrotherbot.net/
Name: {group}\web\{cm:Manual,Manual}; Filename: http://wiki.github.com/BigBrotherBot/big-brother-bot/manual
Name: {group}\web\{cm:Forums,B3 Forums}; Filename: http://forum.bigbrotherbot.net/
Name: {group}\web\{cm:DownloadPlugins,Download plugins}; Filename: http://forum.bigbrotherbot.net/downloads/?cat=4
Name: {group}\web\{cm:B3configGenerator,B3 config generator}; Filename: http://config.bigbrotherbot.net/; 
Name: {group}\web\artwork; Filename: http://www.bigbrotherbot.net/logos
Name: {group}\web\other tools\{cm:Echelon,Echelon}; Filename: http://echelon.bigbrotherbot.net/
Name: {group}\web\other tools\{cm:Xlrstats,XLRstats}; Filename: http://www.xlrstats.com/

[Dirs]
Name: {commonappdata}\BigBrotherBot; Permissions: users-full

[Files]
Source: ..\..\dist_py2exe\b3_run.exe; DestDir: {app}
Source: ..\..\dist_py2exe\b3.lib; DestDir: {app}
Source: ..\..\dist_py2exe\PKG-INFO; DestDir: {app}
;Source: ..\..\dist_py2exe\README; DestDir: {app}; DestName: README.txt
Source: ..\..\dist_py2exe\docs\*; DestDir: {app}\docs; Flags: recursesubdirs
Source: ..\..\dist_py2exe\sql\*; DestDir: {app}\sql; Flags: recursesubdirs
Source: ..\..\dist_py2exe\extplugins\*; DestDir: {app}\extplugins; Flags: recursesubdirs
Source: ..\..\dist_py2exe\conf\*; DestDir: {commonappdata}\BigBrotherBot\conf; Flags: recursesubdirs
Source: b3.ico; DestDir: {app}
Source: b3-plugins-icon.ico; DestDir: {app}



[Components]


[UninstallDelete]
Name: {app}\*; Type: filesandordirs


[CustomMessages]
Website=BigBrotherBot Website
Forums=Forums
Manual=Manual
B3ConfDir=config folder
extplugins=plugins folder
configWizard=Run B3 config wizard
executable=Run B3
DownloadPlugins=Download more plugins
Echelon=Echelon
Xlrstats=XLRstats
B3configGenerator=B3 config generator
sql=sql folder
docs=docs folder
