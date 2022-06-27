# Why
Die AdGuard App von iOS spuckt bei einem Export ein Verzeichnis mit Datei aus.
Die Datei um die es geht liegt im Verzeichnis "Targets" und lautet "com.adguard.AdguardPro.tunnel".
Des Weiteren sieht das Log wie folgt aus (Beispiel):

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

Das ist nicht das was ich möchte. Ich möchte nur die URLs haben, die Versucht werden aufzurufen.
In der Log Datei wären das die Zeilen mit dem Event "handleEvent domain:" und der jeweiligen URL die danach folgt.
Wenn ich die URLs haben, dann kann ich diese mit dem Projekt https://github.com/b3ncha/blocklists abgleichen und die fehlenden URLs hinzufügen.

