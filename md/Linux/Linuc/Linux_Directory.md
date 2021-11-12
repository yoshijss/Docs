## Linux Directory

### /boot
* /boot/efi
  EFIシステムパーティション
* /boot/grub/grub.cfg
  BIOSのGRUB設定ファイル
* /boot/efi/EFI/<id>/grub.cfg
  UEFIのGRUB設定ファイル

### /etc
* /etc/default/grub
  GRUBの設定
* /etc/systemd/system
  カスタマイズしたsystemdのUnitが配置されている   
* /etc/systemd/system/default.target
  systemdでまず起動するUnit

### /proc
* /proc/cmdline
  起動オプションが書かれているファイル
* /proc/version
  システム情報が書かれているファイル

### /usr
* /usr/lib/systemd/system
  デフォルトのsystemdのUnit