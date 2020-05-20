title: Sansa Clip+ Battery Replacement
date: 2018-11-20

Although the Sansa Clip+ was released almost 10 years ago, it is still an extremely desirable digital audio player. Its ability to run the open source software [Rockbox](https://www.rockbox.org/), a small form factor and excellent battery life are all factors of its popularity. Unfortunately SanDisk has discontinued the model, and that excellent battery life doesn't last forever.

![](/static/images/blog/sansa-battery/sansa_battery_small_orig.jpg)
<small>Fig 1. The original battery (with integrated circuit removed)</small>

The OEM battery measures 30mm x 36mm x 3mm, which is virtually impossible to find online. However, it is possible to find a battery slightly smaller that will fit. At 30mm x 30mm x 3mm, the 303030 is a good fit. You can pick up 5 of these on [eBay](https://www.ebay.co.uk/itm/5-pcs-3-7v-240mAh-Li-Po-Battery-Cell-303030-for-MP3-Bluetooth-Headset-Smart-Band/183293761096) for just £10.

![](/static/images/blog/sansa-battery/sansa_battery_small_303030.jpg)
<small>Fig 2. The replacement battery</small>

These batteries only have 2 wires whilst the original has 3. At first this seemed an issue, as the third wire is generally used for an internal temperature sensor, and a lot electronics refuse to work without one. Because of this I attempted to transplant the original battery's integrated circuit, however this must have tripped the safety fuse on the IC, resulting in 0 volts being output.

![](/static/images/blog/sansa-battery/sansa_battery_small_open.jpg)
<small>Fig 3. The new battery attached</small>

Luckily, it seems the third wire isn't actually required on the Sansa. After trimming the wires and soldering the new battery onto the board, the device was able to boot.

![](/static/images/blog/sansa-battery/sansa_battery_small_folded.jpg)
<small>Fig 4. The new battery positioned correctly</small>

The IC on the 303030s come positioned in a way that make them slightly thicker than the cell itself, this can cause the battery to not sit properly on the board. By carefully bending the IC back, you can ensure excessive pressure isn't put on the new battery.

Closing the device properly can be quite time consuming, and [care is needed](https://www.youtube.com/watch?v=beMcITVdZcE) when opening or closing it to prevent damage to cell and plastic casing.

My once dead player seems to work perfectly now. Playback time is slightly less than out-of-the-box, as a 240mAh battery was used instead of the OEM's 290mAh. However it is possible to purchase [280mAh 303030s](https://www.ebay.co.uk/itm/3-7-V-280mAh-303030-Li-Polymer-Rechargeable-Cell-Li-ion-LiPo-Battery-for-GPS-MP3/192602681960). For anyone attempting this repair who encounters any issues charging, it may be related to the lack of a 3rd wire on the new battery's IC. If this is the case, it should be possible to [fix this](https://electronics.stackexchange.com/questions/152053/replace-3-wires-tablet-battery-with-2-wires-one/152058#152058) by soldering a 10kilo ohm resistor between the T pin and ground. Just remember to take care when playing with batteries.


