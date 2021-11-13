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

### /lib
* /lib/modules/カーネルバージョン
  カーネルモジュールのインストール先

### /proc
* /proc/cmdline
  起動オプションが書かれているファイル
* /proc/version
  システム情報が書かれているファイル

### /usr
* /usr/lib/systemd/system
  デフォルトのsystemdのUnit
* /usr/src/linux
  カーネルのソースコード
* /usr/src/linux/arch
  アーキテクチャに依存したコード
* /usr/src/linux/configs
  目的別の.configファイル
* /usr/src/linux/crypto
  暗号処理関数
* /usr/src/linux/drivers
  各種デバイスドライバ関連
* /usr/src/linux/fs
  仮想ファイルシステムと各種ファイルシステム関連
* /usr/src/linux/include
  C言語のインクルードファイル
* /usr/src/linux/init
  初期化コード
* /usr/src/linux/ipc
  SystemV互換プロセス間通信関連(共有メモリ、セマフォなど)
* /usr/src/linux/kernel
  主要なカーネル機能
* /usr/src/linux/lib
  各種モジュール関連
* /usr/src/linux/mm
  メモリ管理関連
* /usr/src/linux/net
  各種ネットワークプロトコル関連
* /usr/src/linux/scripts
  カーネル作成支援スクリプト
* /usr/src/linux/Documentation
  各種ドキュメント
* /usr/src/linux/.config
  カーネルの設定ファイル
* /usr/src/linux/Makefile
  カーネルのMakefile







