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

Bu repoda workspace repo kokundeki `otonomus_ws/` klasorunun icindedir. Bu nedenle once repoyu klonlayip sonra workspace klasorune girmeniz gerekir.

```bash
git clone https://github.com/MasterLoki0616/oib_otonomus.git
cd oib_otonomus/otonomus_ws
```

## Guncel Degisiklikleri Cekme

Repodaki son degisiklikleri almak icin:

```bash
cd ~/oib_otonomus
git pull origin main
```

Isterseniz once durum kontrolu de yapabilirsiniz:

```bash
cd ~/oib_otonomus
git status
git pull origin main
```

## Workspace Yapisi

Paket bu konumdadir:

```bash
~/oib_otonomus/otonomus_ws/src/self_driving_car_pkg
```

Bu repoda workspace `otonomus_ws/` klasoru altindadir ve `build`, `install`, `log` ve `src` klasorlerinin tamami burada bulunur.

## Onemli: Clone Sonrasi Hemen Build Edin

Bu proje klonlandiktan veya dosyalar guncellendikten sonra `colcon build` komutu mutlaka calistirilmalidir. Aksi takdirde mevcut `build` ve `install` ciktilari sizin sisteminize uygun olmayabilir ve launch dosyalari dogru sekilde calismayabilir.

```bash
cd ~/oib_otonomus/otonomus_ws
source /opt/ros/foxy/setup.bash
colcon build
```

Build bittikten sonra:

```bash
source ~/oib_otonomus/otonomus_ws/install/setup.bash
```

## .bashrc Ayari

Her terminal acilisinda tekrar tekrar `source` yazmamak icin asagidaki satirlari `~/.bashrc` dosyaniza ekleyin:

```bash
source /opt/ros/foxy/setup.bash
source ~/oib_otonomus/otonomus_ws/install/setup.bash
export GAZEBO_PLUGIN_PATH=$GAZEBO_PLUGIN_PATH:/usr/lib/x86_64-linux-gnu/gazebo-11/plugins
export GAZEBO_MODEL_PATH=$GAZEBO_MODEL_PATH:/home/$USER/oib_otonomus/otonomus_ws/src/self_driving_car_pkg/models
```

Notlar:

- Buradaki `$USER` ifadesi otomatik olarak kendi Linux kullanici adinizi kullanir.
- Eger repoyu farkli bir klasore klonlarsaniz, `source ~/oib_otonomus/otonomus_ws/install/setup.bash` ve `GAZEBO_MODEL_PATH` satirlarini kendi klasor yolunuza gore duzenleyin.
- `source ~/oib_otonomus/otonomus_ws/install/setup.bash` satirinin sorunsuz calismasi icin once en az bir kez `colcon build` calistirilmis olmalidir.

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
source ~/oib_otonomus/otonomus_ws/install/setup.bash
```

## Tipik Kullanim Sirasi

```bash
git clone https://github.com/MasterLoki0616/oib_otonomus.git
cd oib_otonomus/otonomus_ws
source /opt/ros/foxy/setup.bash
colcon build
source ~/oib_otonomus/otonomus_ws/install/setup.bash
ros2 launch self_driving_car_pkg world_gazebo.launch.py
```

## Faydali Komutlar

Projeyi tekrar derlemek icin:

```bash
cd ~/oib_otonomus/otonomus_ws
source /opt/ros/foxy/setup.bash
colcon build
```

Temiz bir terminalde manuel ortam yuklemek icin:

```bash
source /opt/ros/foxy/setup.bash
source ~/oib_otonomus/otonomus_ws/install/setup.bash
```

## Not

Bu repo tam bir `otonomus_ws` workspace goruntusu olarak paylasilmistir. Yine de `build`, `install` ve `log` klasorleri makineye gore degisebildigi icin, projeyi klonladiktan sonra mutlaka yeniden `colcon build` calistirin.
