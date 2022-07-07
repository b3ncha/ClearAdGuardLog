Version: 1.0.0

Workt with: MacOS X 12.4

# Why
The AdGuard app from iOS creats a directory with a files during an export.
The file in question is located in the "Targets" directory and is called "com.adguard.AdguardPro.tunnel".
Furthermore, the log looks like this (example):

    -------------------------------------------------------------
    LOG FILE: com.adguard.AdguardPro.tunnel 2022-06-12--16-28-07-653.log
    -------------------------------------------------------------
    2022/06/12 18:29:05:182 [446110(DnsAdGuardSDK.DnsRequestProcessedEventHandler.eventQueue)]  handleEvent domain: dns.google.com. answer:  status: REFUSED rules: ["||google.com^$important"] type: AAAA whitelst: false upstreamId: 0
    2022/06/12 18:29:05:212 [446110(DnsAdGuardSDK.DnsRequestProcessedEventHandler.eventQueue)]  (ActivityStatistics) - adding a record for dns.google.com.
    2022/06/12 18:29:05:301 [446110(DnsAdGuardSDK.DnsRequestProcessedEventHandler.eventQueue)]  (ActivityStatistics) - record for dns.google.com. has been added
    2022/06/12 18:29:05:315 [446110(DnsAdGuardSDK.DnsRequestProcessedEventHandler.eventQueue)]  handleEvent domain: dns.google.com. answer:  status: REFUSED rules: ["||google.com^$important"] type: A whitelst: false upstreamId: 0
    2022/06/12 18:29:05:316 [446110(DnsAdGuardSDK.DnsRequestProcessedEventHandler.eventQueue)]  (ActivityStatistics) - adding a record for dns.google.com.
    2022/06/12 18:29:05:322 [446110(DnsAdGuardSDK.DnsRequestProcessedEventHandler.eventQueue)]  (ActivityStatistics) - record for dns.google.com. has been added
    2022/06/12 18:29:05:335 [446110(DnsAdGuardSDK.DnsRequestProcessedEventHandler.eventQueue)]  handleEvent domain: dns.google.com. answer:  status: REFUSED rules: ["||google.com^$important"] type: HTTPS whitelst: false upstreamId: 0
    2022/06/12 18:29:05:335 [446110(DnsAdGuardSDK.DnsRequestProcessedEventHandler.eventQueue)]  (ActivityStatistics) - adding a record for dns.google.com.
    2022/06/12 18:29:05:342 [446110(DnsAdGuardSDK.DnsRequestProcessedEventHandler.eventQueue)]  (ActivityStatistics) - record for dns.google.com. has been added
    2022/06/12 18:29:05:362 [446110(DnsAdGuardSDK.DnsRequestProcessedEventHandler.eventQueue)]  handleEvent domain: gateway.icloud.com. answer:  status: REFUSED rules: ["||gateway.icloud.com^$important"] type: AAAA whitelst: false upstreamId: 0
    2022/06/12 18:29:05:362 [446110(DnsAdGuardSDK.DnsRequestProcessedEventHandler.eventQueue)]  (ActivityStatistics) - adding a record for gateway.icloud.com.
    2022/06/12 18:29:05:369 [446110(DnsAdGuardSDK.DnsRequestProcessedEventHandler.eventQueue)]  (ActivityStatistics) - record for gateway.icloud.com. has been added
    2022/06/12 18:29:05:384 [446110(DnsAdGuardSDK.DnsRequestProcessedEventHandler.eventQueue)]  handleEvent domain: gateway.icloud.com. answer:  status: REFUSED rules: ["||gateway.icloud.com^$important"] type: HTTPS whitelst: false upstreamId: 0
    2022/06/12 18:29:05:385 [446110(DnsAdGuardSDK.DnsRequestProcessedEventHandler.eventQueue)]  (ActivityStatistics) - adding a record for gateway.icloud.com.
    2022/06/12 18:29:05:391 [446110(DnsAdGuardSDK.DnsRequestProcessedEventHandler.eventQueue)]  (ActivityStatistics) - record for gateway.icloud.com. has been added
    2022/06/12 18:29:05:406 [446110(DnsAdGuardSDK.DnsRequestProcessedEventHandler.eventQueue)]  handleEvent domain: gateway.icloud.com. answer:  status: REFUSED rules: ["||gateway.icloud.com^$important"] type: A whitelst: false upstreamId: 0

This is not what I want. I only want to have the URLs that are tried to be called or could be called.
In the log file these would be the lines with the event "handleEvent domain:" and the respective URL that follows.
If I have the URLs, then I can match them with the project https://github.com/b3ncha/blocklists and add the missing URLs.

# USE
## Requirements
You need python 3.10.x and you need the file "clearadguardlog.py". Nothing more.

## run

    python3 clearadguardlog.py -i <adguard.tunnel file>


# Develpment
## Requirements

1. python3
2. pipenv (https://pipenv.pypa.io/en/latest/, https://github.com/pypa/pipenv)
3. editor like vscode

## You like to edit and test, do this:

    git clone https://github.com/b3ncha/ClearAdGuardLog

    cd ClearAdGuardLog

    pipenv install

    pipenv shell

## vscode
If you are using Visual Studio Code and you have already run "pipenv install", then take a look in the .vscode directory and check the "settings.json" file.
The path for "python.defaultInterpreterPath" might be different. You can test this if you run "pipenv --py" and compare the directories.
Why do I need this? VSCode can access python directly in the pipenv environment with this setting without starting the "pipenv shell" first.
Otherwise VScode uses the installed version of your Mac, Linux or Windows.

## Dev work done
Their work is done and uploaded, then they can clean up their workspace with the following command:

    pipenv uninstall --all

# Bug
You have found an error, then open a case.

# To Dos
Nothing in the moment