# oib_otonomus

Bu repo, ROS 2 Foxy ve Ubuntu 20.04 uzerinde calistirilmak uzere hazirlanmis `self_driving_car_pkg` paketini ve ilgili Gazebo dunya dosyalarini icerir.

## Gereksinimler

- Ubuntu 20.04
- ROS 2 Foxy
- Gazebo 11
- `python3-colcon-common-extensions`

Ornek kurulum:

```bash
sudo apt update
sudo apt install -y ros-foxy-desktop ros-foxy-gazebo-ros-pkgs python3-colcon-common-extensions
```

## Repoyu Klonlama

Repoyu dogrudan `~/otonomus_ws` klasorune klonlamaniz tavsiye edilir. Boylece asagidaki `source` ve Gazebo path ayarlari birebir calisir.

```bash
git clone https://github.com/MasterLoki0616/oib_otonomus.git ~/otonomus_ws
cd ~/otonomus_ws
```

## Guncel Degisiklikleri Cekme

Repodaki son degisiklikleri almak icin:

```bash
cd ~/otonomus_ws
git pull origin main
```

Isterseniz once durum kontrolu de yapabilirsiniz:

```bash
cd ~/otonomus_ws
git status
git pull origin main
```

## Workspace Yapisi

Paket bu konumdadir:

```bash
~/otonomus_ws/src/self_driving_car_pkg
```

Bu repoda yalnizca `src` degil, `otonomus_ws` icindeki `build`, `install`, `log` ve `src` klasorlerinin tamami bulunur.

## Onemli: Clone Sonrasi Hemen Build Edin

Bu proje klonlandiktan veya dosyalar guncellendikten sonra `colcon build` komutu mutlaka calistirilmalidir. Aksi takdirde mevcut `build` ve `install` ciktilari sizin sisteminize uygun olmayabilir ve launch dosyalari dogru sekilde calismayabilir.

```bash
cd ~/otonomus_ws
source /opt/ros/foxy/setup.bash
colcon build
```

Build bittikten sonra:

```bash
source ~/otonomus_ws/install/setup.bash
```

## .bashrc Ayari

Her terminal acilisinda tekrar tekrar `source` yazmamak icin asagidaki satirlari `~/.bashrc` dosyaniza ekleyin:

```bash
source /opt/ros/foxy/setup.bash
source ~/otonomus_ws/install/setup.bash
export GAZEBO_PLUGIN_PATH=$GAZEBO_PLUGIN_PATH:/usr/lib/x86_64-linux-gnu/gazebo-11/plugins
export GAZEBO_MODEL_PATH=$GAZEBO_MODEL_PATH:/home/$USER/otonomus_ws/src/self_driving_car_pkg/models
```

Notlar:

- Buradaki `$USER` ifadesi otomatik olarak kendi Linux kullanici adinizi kullanir.
- Eger repoyu `~/otonomus_ws` disinda farkli bir klasore klonlarsaniz, `source ~/otonomus_ws/install/setup.bash` ve `GAZEBO_MODEL_PATH` satirlarini kendi klasor yolunuza gore duzenleyin.
- `source ~/otonomus_ws/install/setup.bash` satirinin sorunsuz calismasi icin once en az bir kez `colcon build` calistirilmis olmalidir.

Degisikliklerden sonra `.bashrc` ayarlarini aktif etmek icin:

```bash
source ~/.bashrc
```

## Dunyayi Baslatma

Gazebo dunyasini baslatmak icin:

```bash
ros2 launch self_driving_car_pkg world_gazebo.launch.py
```

Eger yeni bir terminal actiysaniz ve `.bashrc` henuz yuklenmediyse, once sunlari calistirin:

```bash
source /opt/ros/foxy/setup.bash
source ~/otonomus_ws/install/setup.bash
```

## Tipik Kullanim Sirasi

```bash
git clone https://github.com/MasterLoki0616/oib_otonomus.git ~/otonomus_ws
cd ~/otonomus_ws
source /opt/ros/foxy/setup.bash
colcon build
source ~/otonomus_ws/install/setup.bash
ros2 launch self_driving_car_pkg world_gazebo.launch.py
```

## Faydali Komutlar

Projeyi tekrar derlemek icin:

```bash
cd ~/otonomus_ws
source /opt/ros/foxy/setup.bash
colcon build
```

Temiz bir terminalde manuel ortam yuklemek icin:

```bash
source /opt/ros/foxy/setup.bash
source ~/otonomus_ws/install/setup.bash
```

## Not

Bu repo tam bir `otonomus_ws` workspace goruntusu olarak paylasilmistir. Yine de `build`, `install` ve `log` klasorleri makineye gore degisebildigi icin, projeyi klonladiktan sonra mutlaka yeniden `colcon build` calistirin.
