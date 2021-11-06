## Linux Directory

* /boot/efi
  EFIシステムパーティション
* /boot/grub/grub.cfg
  BIOSのGRUB設定ファイル
* /boot/efi/EFI/<id>/grub.cfg
  UEFIのGRUB設定ファイル

* /etc/default/grub
  GRUBの設定
* /etc/systemd/system
  カスタマイズしたsystemdのUnitが配置されている   
* /etc/systemd/system/default.target
  systemdでまず起動するUnit

* /proc/cmdline
  起動オプションが書かれているファイル

* /usr/lib/systemd/system
  デフォルトのsystemdのUnit