---
layout: post
title:  "How to monitor internet speed using cron and speedtest"
date:   2020-06-06 18:00:00 +0100
categories: internet, software
---

I recently defended my PhD thesis remotely (and successfully!)

As my examiners and I were all ordered to remain at home due to the coronavirus pandemic, the viva was done on Zoom. I was concerned that the internet from my mobile hotspot wouldn't be up to the job, so in order to check that we would be OK for the ~3 hour exam, I wrote a short bit of code to **monitor my internet speed**.

The [code](https://github.com/peregrinescode/speedmon) is based on two software utilities, the speedtest cli and cron.

### Speedtest

[Speedtest.net](https://www.speedtest.net/) is a handy website for checking your ping time, download and upload speeds:

<figure>
    <div class="scaled">
        <img class="center" src="/assets/imgs/speedtest-output.png" alt="Speedtest.net output">
    </div>
</figure> 

Importantly, there is also a Linux-native command line interface which we can wrap with a script to track internet speed over time. To schedule such a script to run automatically, we use cron.

### Cron

From [wikipedia](https://en.wikipedia.org/wiki/Cron):
> cron is the time-based job scheduler in Unix-like computer operating systems. cron enables users to schedule jobs (commands or shell scripts) to run periodically at certain times, dates or intervals. It is commonly used to automate system maintenance or administration.

To interact with cron, we create a *crontab* from the command line `crontab -e` with the following format:
```
minute hour day_of_month month day_of_week command
```
where
* *minute* takes values 0 to 59
* *hour*  takes values 0 to 23.
* *day_of_month* takes values 1 to 31.
* *month values* takes values 1 to 12.
* *day_of_week* takes values 0 to 6, with 0 representing Sunday.

We can also use the following symbols:

| Symbol     	 | Description |
| ----------- | ----------- |
| *			 | every possible value |
| , 		 	 | separate multiple values |
| - 		 	 | range values |
| / 		 	 | specify a periodicity |


So to setup a crontab to run a script every 15 minutes:
```(bash)
*/15 * * * * /path/to/script/cron_speedtest.sh
```

### Results

With cron scheduled to run a speedtest every 15 minutes, I monitored my internet connection for several weeks preceding my viva. I have plotted the results, using seaborn and matplotlib, below:

<figure>
    <img class="center" src="/assets/imgs/ross-warren-speed_v_time-NI.png" alt="speedmon output">
    <figcaption>
      My ping time, download and upload results having run a speedtest every 15 minutes for several weeks before my viva.
    </figcaption>
</figure> 

As you can see, my internet connection was fairly consistent throughout the day. There are a few outliers with long ping times which are a result of my phone losing signal. Luckily these drops in signal were rare, and the connection was just about good enough for my entire exam.