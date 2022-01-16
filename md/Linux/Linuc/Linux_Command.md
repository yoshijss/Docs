## Linuxコマンド

# D #
## depmod
- カーネルモジュールの依存関係情報を更新する

# E #
## efibootmgr
- UEFIにおける起動エントリを管理するコマンド

# G #
## grub-mkconfig/grub2-mkconfig
- grub.cfgの生成

## grub2-set-default 0
- デフォルトのカーネルを変更する

## grub2-mkconfig -o /boot/grub2/grub.cfg
- カーネルの設定ファイルを更新する

# I #
## insmod
- カーネルモジュールをロードする

# J #
## journalctl
- systemdのジャーナルを閲覧する

# L #
## lsmod
- ロードされているカーネルモジュールをリスト表示する

# M #
## make all
- すべてのビルドを行う

## make binrpm-pkg
- ビルド済みカーネルとモジュールのRPMパッケージを作成する

## make clean
- .config以外の不要なファイルを削除する

## make config
- カーネルコンフィギュレーションの設定。コンソール上でカーネルオプションごとに設定

## make deb-pkg
- ビルド済みカーネルとモジュールのDebianパッケージを作成する

## make distclean
- デフォルト値を設定した.configを作成する

## make gconfig
- カーネルコンフィギュレーションの設定。X(GNOME)上で設定

## male install
- カーネルをインストールする

## make menuconfig
- カーネルコンフィギュレーションの設定。コンソール上でメニュー形式で表示されているオプション項目を選択する

## make modules
- 動的なモジュールをすべてビルドする

## make modules_install
- カーネルモジュールを適切なディレクトリにインストールする

## make mrproper
- .configやバックアップファイルも含め不要なファイルを削除する

## make rpm
- カーネルをビルド後にRPMパッケージを作成する

## make rpm-pkg
- ソースRPMパッケージを作成する

## make oldconfig
- カーネルコンフィギュレーションの設定。新しい機能の設定のみコンソール上で問い合わせる

## make xconfig
- カーネルコンフィギュレーションの設定。X(KDE)上で設定

## modinfo
- カーネルモジュールの情報を表示する

## modprobe
- 依存関係を解決してカーネルモジュールをロードまたはアンロードする

# R #
## rmmod
- カーネルモジュールをアンロードする

# S #
## sysctl
- カーネルパラメータを設定する

## systemctl
- systemdの管理

## systemd-delta
- オリジナルのUnit設定ファイルを上書きしている設定の確認

# U #
## uname
- システム情報を表示する。カーネル、ハードウェアアーキテクチャ等