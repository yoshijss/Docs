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
* /proc/sys/fs/file-max
  ファイルハンドルの最大数
* /roc/sys/file-nr
  開かれているファイル数、使用されたファイルハンドルの数、
* /proc/sys/kernel/ctrl-alt-del
  [Ctrl]+[Alt]+[Del]キーの動作設定
* /proc/sys/kernel/hostname
  ホスト名
* /proc/sys/kernel/modprobe
  modprobeのパス
* /proc/sys/kernel/hotplug
  ホットプラグ用のプログラムのパス
* /proc/sys/kernel/osrelease
  カーネルバージョン
* /proc/sys/kernel/ostype
  OSの種類
* /proc/sys/kernel/sem
  セマフォ数
* /proc/sys/kernel/shmall
  共有メモリの合計(バイト単位)
* /proc/sys/kernel/shmmax
  共有メモリセグメントの最大値(バイト単位)
* /proc/sys/kernel/shmmni
  共有メモリセグメントの最大数
* /proc/sys/kernel/sysrq
  システム要求キー(Magic SysRq Key)の有効/無効
* /proc/sys/kernel/threads-max
  スレッド(プロセス)の最大数
* /proc/sys/kernel/version
  カーネル構築の情報
* /proc/sys/net/core/rmem_default
  受信ソケットバッファのデフォルトサイズ
* /proc/sys/net/core/rmem_max
  受信ソケットバッファの最大サイズ
* /proc/sys/net/core/wmem_default
  送信ソケットバッファのデフォルトサイズ
* /proc/sys/net/core/wmem_max
  送信ソケットバッファの最大サイズ
* /proc/sys/net/ipv4/ip_forward
  ネットワークインタフェース間でのパケット転送の有効/無効
* /proc/sys/net/ipv4/icmp_echo_ignore_broadcast
  ブロードキャスト宛のICMP Echo Requestを無視するかどうか
* /proc/sys/net/ipv4/icmp_echo_ignore_all
  すべてのICMP Echo Requestを無視するかどうか
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







