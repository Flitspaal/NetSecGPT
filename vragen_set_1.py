hoofdvragen = {
    "1": "Ik wil weten hoe veilig wij zijn?",
    "2": "Ik wil voldoen aan een bepaalde regelgeving, zoals ISO 27001.",
    "3": "Mijn moederbedrijf eist dat wij een pentest uitvoeren.",
    "4": "Ik wil aantonen aan een leverancier hoe veilig we zijn.",
    "5": "We willen ons beveiligingsniveau verhogen en onze systemen verbeteren.",
    "6": "We hebben nieuwe systemen, applicaties of netwerken geïmplementeerd en willen controleren of deze veilig zijn.",
    "7": "We hebben recentelijk personeelsveranderingen gehad en willen ervoor zorgen dat onze beveiliging nog steeds robuust is.",
    "8": "We hebben een contract gewonnen voor een nieuw project of klant, en deze vereist een pentest om te voldoen aan de vereisten van de klant of de regelgeving.",
    "9": "We hebben een vermoeden van kwetsbaarheden in onze systemen en willen deze laten onderzoeken en verifiëren door een expert."
}
subvragen_sets = {
    "1": {
        "1": {
            "text": "Welke systemen en/of netwerken wilt u laten testen?",
            "options": {
                "1": "Externe website: Een website die toegankelijk is vanuit het publieke internet.",
                "2": "Interne website: Een website die alleen toegankelijk is vanuit uw bedrijfsnetwerk.",
                "3": "Desktop software: Een desktopapplicatie die op uw bedrijfsnetwerk draait.",
                "4": "Mobiele applicatie: Een mobiele app die op iOS of Android draait.",
                "5": "Bedrijfsnetwerk: Een interne bedrijfsnetwerk met meerdere servers, computers en apparaten.",
                "6": "Medewerkers: Het bewustzijn van uw medewerkers testen met betrekking tot informatiebeveiliging.",
                "7": "Cloudinfrastructuur: Een cloudgebaseerde infrastructuur zoals AWS of Azure.",
                "8": "Extern netwerk: Een netwerk dat toegankelijk is vanaf het internet.",
                "9": "Interne netwerken: Interne bedrijfsnetwerken met meerdere servers, computers en apparaten.",
                "10": "Draadloze netwerken: Wifi-netwerken die toegankelijk zijn voor het publiek of binnen uw organisatie.",
                "11": "Internet of Things (IoT): Apparaten die met het internet zijn verbonden, zoals slimme thermostaten, beveiligingscamera's en slimme speakers."
            }
        },
        "2": {
            "text": "Welk pentestscenario past het beste bij uw behoeften? Selecteer de situatie die het beste bij u past:",
            "options": {
                "1": "White Box: De Pentester krijgt volledige kennis van het doelsysteem, inclusief de broncode en de architectuur van het systeem. ",
                "2": "Grey Box: De Pentester krijgt (beperkte) toegang tot de systeeminformatie die normaal gesproken beschikbaar is voor alleen geautoriseerde gebruikers (bijvoorbeeld een werknemer).",
                "3": "Black Box: De Pentester krijgt geen voorkennis van het doelsysteem dat wordt getest. Dus geen voorkennis van de interne werking, het architectuur OF de broncode. "
            }
        },
        "3": {
            "text": "Heeft u eerder in het verleden penetratietesten uitgevoerd?",
            "options": {
                "1": "Ja",
                "2": "Nee",
                "3": "Ik geef het liever niet aan"
            }
        },
        "4": {
        "text": "Welke beveiligingsmaatregelen heeft u momenteel geïmplementeerd?",
        "options": {
            "1": "Security monitoring",
            "2": "Firewalls",
            "3": "Data-encryptie",
            "4": "Access control",
            "5": "Multi-factor authenticatie",
            "6": "Security Information and Event Management (SIEM)",
            "7": "Security policies and procedures",
            "8": "Security awareness training",
            "9": "Penetration testing and vulnerability scanning",
            "10": "Geen van boven genoemde maatregelen",
            "11": "Ik geef het liever niet aan"
            }
        },
        "5": {
        "text": "Heeft u de afgelopen zes maanden te maken gehad met beveiligingsincidenten?",
        "options": {
            "1": "Nee",
            "2": "Ja",
            "3": "Ik geef het liever niet aan"
            }
        },
        "6": {
        "text": "Welke potentiële beveiligingsrisico's maakt u zich het meest zorgen over?",
        "options": {
            "1": "Datalekken",
            "2": "Phishingaanvallen",
            "3": "Ransomware",
            "4": "Ongeautoriseerde toegang",
            "5": "DDoS-aanvallen",
            "6": "Malware",
            "7": "Insider bedreigingen",
            "8": "Onveilige webapplicaties",
            "9": "Slechte wachtwoordbeveiliging",
            "10": "Slecht beheerde netwerkapparatuur",
            "11": "Geen van bovengenoemde maatregelen",
            "12": "Ik geef het liever niet aan"
            }
        },
    }, 
    "2" : {
        "1": {
            "text": "Welke systemen en netwerken wilt u laten testen? Selecteer de situatie die het beste bij u past:",
            "options": {
                "1": "Externe website: Een website die toegankelijk is vanuit het publieke internet.",
                "2": "Interne website: Een website die alleen toegankelijk is vanuit uw bedrijfsnetwerk.",
                "3": "Desktop software: Een desktopapplicatie die op uw bedrijfsnetwerk draait.",
                "4": "Mobiele applicatie: Een mobiele app die op iOS of Android draait.",
                "5": "Bedrijfsnetwerk: Een interne bedrijfsnetwerk met meerdere servers, computers en apparaten.",
                "6": "Medewerkers: Het bewustzijn van uw medewerkers testen met betrekking tot informatiebeveiliging.",
                "7": "Cloudinfrastructuur: Een cloudgebaseerde infrastructuur zoals AWS of Azure.",
                "8": "Extern netwerk: Een netwerk dat toegankelijk is vanaf het internet.",
                "9": "Interne netwerken: Interne bedrijfsnetwerken met meerdere servers, computers en apparaten.",
                "10": "Draadloze netwerken: Wifi-netwerken die toegankelijk zijn voor het publiek of binnen uw organisatie.",
                "11": "Internet of Things (IoT): Apparaten die met het internet zijn verbonden, zoals slimme thermostaten, beveiligingscamera's en slimme speakers."
            }
        },
        "2": {
            "text": "Welk pentestscenario past het beste bij uw behoeften? Selecteer de situatie die het beste bij u past:",
            "options": {
                "1": "White Box: De Pentester krijgt volledige kennis van het doelsysteem, inclusief de broncode en de architectuur van het systeem. ",
                "2": "Grey Box: De Pentester krijgt (beperkte) toegang tot de systeeminformatie die normaal gesproken beschikbaar is voor alleen geautoriseerde gebruikers (bijvoorbeeld een werknemer).",
                "3": "Black Box: De Pentester krijgt geen voorkennis van het doelsysteem dat wordt getest. Dus geen voorkennis van de interne werking, het architectuur OF de broncode. "
            }
        },
        "3": {
        "text": "Welke specifieke vereisten van de regelgeving moet u naleven?",
        "options": {
            "1": "ISO 27001",
            "2": "NEN7510",
            "3": "AVG/GDPR",
            "4": "HIPAA",
            "5": "PCI-DSS",
            "6": "SOX",
            "7": "FISMA",
            "8": "GLBA",
            "9": "CCPA",
            "10": "CMMC",
            "11": "NIST SP 800-171",
            "12": "EI3PA",
            "13": "SWIFT CSCF",
            "14": "CTPAT",
            "15": "ISO 20000-1",
            "16": "Geen van bovengenoemde",
            "17": "Ik geef het liever niet aan"
            }
        },
        "4": {
            "text": "Heeft u al maatregelen geïmplementeerd om te voldoen aan deze vereisten?",
            "options": {
            "1": "Ja",
            "2": "Nee",
            "3": "Gedeeltelijk",
            "4": "Ik geef het liever niet aan"
            }
        },
        "5": {
            "text": "Zijn er bepaalde beveiligingsrisico's waar u zich zorgen over maakt met betrekking tot de regelgeving?",
            "options": {
            "1": "Phishingaanvallen",
            "2": "Ransomware",
            "3": "Malware",
            "4": "Datalekken",
            "5": "Ongeautoriseerde toegang",
            "6": "Slecht beheerde netwerkapparatuur",
            "7": "DDoS-aanvallen",
            "8": "Insider bedreigingen",
            "9": "Onveilige webapplicaties",
            "10": "Slechte wachtwoordbeveiliging",
            "11": "Ik geef het liever niet aan"
            }
        },
        "6": {
            "text": "Is uw huidige beveiligingsbeleid in overeenstemming met de regelgeving?",
            "options": {
            "1": "Ja",
            "2": "Nee",
            "3": "Gedeeltelijk",
            "4": "Ik geef het liever niet aan"
            }
        },
    },
    "3" : {
        "1": {
            "text": "Welke systemen en netwerken wilt u laten testen? Selecteer de situatie die het beste bij u past:",
            "options": {
                "1": "Externe website: Een website die toegankelijk is vanuit het publieke internet.",
                "2": "Interne website: Een website die alleen toegankelijk is vanuit uw bedrijfsnetwerk.",
                "3": "Desktop software: Een desktopapplicatie die op uw bedrijfsnetwerk draait.",
                "4": "Mobiele applicatie: Een mobiele app die op iOS of Android draait.",
                "5": "Bedrijfsnetwerk: Een interne bedrijfsnetwerk met meerdere servers, computers en apparaten.",
                "6": "Medewerkers: Het bewustzijn van uw medewerkers testen met betrekking tot informatiebeveiliging.",
                "7": "Cloudinfrastructuur: Een cloudgebaseerde infrastructuur zoals AWS of Azure.",
                "8": "Extern netwerk: Een netwerk dat toegankelijk is vanaf het internet.",
                "9": "Interne netwerken: Interne bedrijfsnetwerken met meerdere servers, computers en apparaten.",
                "10": "Draadloze netwerken: Wifi-netwerken die toegankelijk zijn voor het publiek of binnen uw organisatie.",
                "11": "Internet of Things (IoT): Apparaten die met het internet zijn verbonden, zoals slimme thermostaten, beveiligingscamera's en slimme speakers."
            }
        },
        "2": {
            "text": "Welk pentestscenario past het beste bij uw behoeften? Selecteer de situatie die het beste bij u past:",
            "options": {
                "1": "White Box: De Pentester krijgt volledige kennis van het doelsysteem, inclusief de broncode en de architectuur van het systeem. ",
                "2": "Grey Box: De Pentester krijgt (beperkte) toegang tot de systeeminformatie die normaal gesproken beschikbaar is voor alleen geautoriseerde gebruikers (bijvoorbeeld een werknemer).",
                "3": "Black Box: De Pentester krijgt geen voorkennis van het doelsysteem dat wordt getest. Dus geen voorkennis van de interne werking, het architectuur OF de broncode. "
            }
        },
        "3": {
        "text": "Welke beveiligingsrisico's ziet uw moederbedrijf dat u moet aanpakken?",
        "options": {
            "1": "Mogelijk ongeautoriseerde toegang tot gevoelige informatie of systemen",
            "2": "Gebruik van zwakke of herbruikbare wachtwoorden",
            "3": "Ontbrekende of verouderde beveiligingspatches op systemen of applicaties",
            "4": "Risico's die voortvloeien uit het gebruik van externe leveranciers of partners",
            "5": "Onvoldoende beveiliging van mobiele apparaten die toegang hebben tot bedrijfsinformatie",
            "6": "Gebrek aan bewustzijn van medewerkers over beveiligingsprotocollen en -procedures",
            "7": "Risico's die voortvloeien uit onvoldoende fysieke beveiliging van bedrijfsmiddelen of -gebouwen.",
            "8": "Ik geef het liever niet aan"
            }
        },
        "4": {
            "text": "Heeft uw moederbedrijf specifieke vereisten voor de pentest?",
            "options": {
            "1": "Ja",
            "2": "Nee",
            "3": "Gedeeltelijk",
            "4": "Ik geef het liever niet aan"
            }
        },
        "5": {
            "text": "Welk tijdsbestek heeft uw moederbedrijf vastgesteld voor de uitvoering van de pentest?",
            "options": {
            "1": "Minder dan een maand",
            "2": "Minder dan drie maanden",
            "3": "Minder dan zes maanden",
            "4": "Meer dan zes maanden",
            "5": "Geen vastgesteld tijdsbestek",
            "6": "Ik geef het liever niet aan"
            }
        },
        "6": {
            "text": "Welke impact kan het niet uitvoeren van de pentest hebben op uw bedrijfsrelatie met uw moederbedrijf",
            "options": {
            "1": "Verlies van vertrouwen: Het niet uitvoeren van de pentest kan ervoor zorgen dat uw moederbedrijf het vertrouwen in uw beveiligingsmaatregelen verliest en twijfelt aan uw vermogen om gevoelige informatie te beschermen.",
            "2": "Contractbreuk: Als het uitvoeren van een pentest contractueel is overeengekomen en u dit niet nakomt, kunt u mogelijk in strijd zijn met het contract en kan uw moederbedrijf stappen ondernemen om dit te verhelpen.",
            "3": "Vertraging van projecten: Het niet uitvoeren van een pentest kan ertoe leiden dat projecten worden vertraagd of zelfs stopgezet als uw moederbedrijf niet zeker is van de veiligheid van uw systemen en netwerken.",
            "4": "Negatieve publiciteit: Als het niet uitvoeren van een pentest leidt tot beveiligingsincidenten of gegevenslekken, kan dit leiden tot negatieve publiciteit voor uw bedrijf en mogelijk schade toebrengen aan uw reputatie.",
            "5": "Financiële gevolgen: Het niet uitvoeren van een pentest kan mogelijk financiële gevolgen hebben, bijvoorbeeld als uw moederbedrijf besluit om boetes op te leggen of om kosten te verhalen die het gevolg zijn van beveiligingsincidenten.",
            "6": "Ik geef het liever niet aan"
            }
        },
    },
    "4" : {
        "1": {
            "text": "Welke systemen en netwerken wilt u laten testen? Selecteer de situatie die het beste bij u past:",
            "options": {
                "1": "Externe website: Een website die toegankelijk is vanuit het publieke internet.",
                "2": "Interne website: Een website die alleen toegankelijk is vanuit uw bedrijfsnetwerk.",
                "3": "Desktop software: Een desktopapplicatie die op uw bedrijfsnetwerk draait.",
                "4": "Mobiele applicatie: Een mobiele app die op iOS of Android draait.",
                "5": "Bedrijfsnetwerk: Een interne bedrijfsnetwerk met meerdere servers, computers en apparaten.",
                "6": "Medewerkers: Het bewustzijn van uw medewerkers testen met betrekking tot informatiebeveiliging.",
                "7": "Cloudinfrastructuur: Een cloudgebaseerde infrastructuur zoals AWS of Azure.",
                "8": "Extern netwerk: Een netwerk dat toegankelijk is vanaf het internet.",
                "9": "Interne netwerken: Interne bedrijfsnetwerken met meerdere servers, computers en apparaten.",
                "10": "Draadloze netwerken: Wifi-netwerken die toegankelijk zijn voor het publiek of binnen uw organisatie.",
                "11": "Internet of Things (IoT): Apparaten die met het internet zijn verbonden, zoals slimme thermostaten, beveiligingscamera's en slimme speakers."
            }
        },
        "2": {
            "text": "Welk pentestscenario past het beste bij uw behoeften? Selecteer de situatie die het beste bij u past:",
            "options": {
                "1": "White Box: De Pentester krijgt volledige kennis van het doelsysteem, inclusief de broncode en de architectuur van het systeem. ",
                "2": "Grey Box: De Pentester krijgt (beperkte) toegang tot de systeeminformatie die normaal gesproken beschikbaar is voor alleen geautoriseerde gebruikers (bijvoorbeeld een werknemer).",
                "3": "Black Box: De Pentester krijgt geen voorkennis van het doelsysteem dat wordt getest. Dus geen voorkennis van de interne werking, het architectuur OF de broncode. "
            }
        },
        "3": {
        "text": "Welke specifieke beveiligingsstandaarden hanteert uw leverancier?",
        "options": {
            "1": "ISO 27001",
            "2": "PCI DSS",
            "3": "HIPAA",
            "4": "NIST SP 800-53",
            "5": "SOC 2",
            "6": "GDPR",
            "7": "FedRAMP",
            "8": "FISMA",
            "9": "GLBA",
            "10": "SOX",
            "11": "CSA STAR",
            "12": "Ik geef het liever niet aan"
            }
        },
        "4": {
            "text": "Heeft uw leverancier specifieke eisen voor de pentest?",
            "options": {
            "1": "Ja",
            "2": "Nee",
            "3": "Gedeeltelijk",
            "4": "Ik geef het liever niet aan"
            }
        },
        "5": {
            "text": "Welk tijdsbestek heeft uw moederbedrijf vastgesteld voor de uitvoering van de pentest?",
            "options": {
            "1": "Minder dan een maand",
            "2": "Minder dan drie maanden",
            "3": "Minder dan zes maanden",
            "4": "Meer dan zes maanden",
            "5": "Geen vastgesteld tijdsbestek",
            "6": "Ik geef het liever niet aan"
            }
        },
        "6": {
            "text": "Welke impact kan het niet uitvoeren van de pentest hebben op uw bedrijfsrelatie met uw leverancier?",
            "options": {
            "1": "Verlies van vertrouwen: Het niet uitvoeren van de pentest kan ervoor zorgen dat uw leverancier het vertrouwen in uw beveiligingsmaatregelen verliest en twijfelt aan uw vermogen om gevoelige informatie te beschermen.",
            "2": "Contractbreuk: Als het uitvoeren van een pentest contractueel is overeengekomen en u dit niet nakomt, kunt u mogelijk in strijd zijn met het contract en kan uw leverancier stappen ondernemen om dit te verhelpen.",
            "3": "Vertraging van projecten: Het niet uitvoeren van een pentest kan ertoe leiden dat projecten worden vertraagd of zelfs stopgezet als uw leverancier niet zeker is van de veiligheid van uw systemen en netwerken.",
            "4": "Negatieve publiciteit: Als het niet uitvoeren van een pentest leidt tot beveiligingsincidenten of gegevenslekken, kan dit leiden tot negatieve publiciteit voor uw bedrijf en mogelijk schade toebrengen aan uw reputatie.",
            "5": "Financiële gevolgen: Het niet uitvoeren van een pentest kan mogelijk financiële gevolgen hebben, bijvoorbeeld als uw leverancier besluit om boetes op te leggen of om kosten te verhalen die het gevolg zijn van beveiligingsincidenten.",
            "6": "Ik geef het liever niet aan"
            }
        },
    },
    "5" : {
        "1": {
            "text": "Welke systemen en netwerken wilt u laten testen? Selecteer de situatie die het beste bij u past:",
            "options": {
                "1": "Externe website: Een website die toegankelijk is vanuit het publieke internet.",
                "2": "Interne website: Een website die alleen toegankelijk is vanuit uw bedrijfsnetwerk.",
                "3": "Desktop software: Een desktopapplicatie die op uw bedrijfsnetwerk draait.",
                "4": "Mobiele applicatie: Een mobiele app die op iOS of Android draait.",
                "5": "Bedrijfsnetwerk: Een interne bedrijfsnetwerk met meerdere servers, computers en apparaten.",
                "6": "Medewerkers: Het bewustzijn van uw medewerkers testen met betrekking tot informatiebeveiliging.",
                "7": "Cloudinfrastructuur: Een cloudgebaseerde infrastructuur zoals AWS of Azure.",
                "8": "Extern netwerk: Een netwerk dat toegankelijk is vanaf het internet.",
                "9": "Interne netwerken: Interne bedrijfsnetwerken met meerdere servers, computers en apparaten.",
                "10": "Draadloze netwerken: Wifi-netwerken die toegankelijk zijn voor het publiek of binnen uw organisatie.",
                "11": "Internet of Things (IoT): Apparaten die met het internet zijn verbonden, zoals slimme thermostaten, beveiligingscamera's en slimme speakers."
            }
        },
        "2": {
            "text": "Welk pentestscenario past het beste bij uw behoeften? Selecteer de situatie die het beste bij u past:",
            "options": {
                "1": "White Box: De Pentester krijgt volledige kennis van het doelsysteem, inclusief de broncode en de architectuur van het systeem. ",
                "2": "Grey Box: De Pentester krijgt (beperkte) toegang tot de systeeminformatie die normaal gesproken beschikbaar is voor alleen geautoriseerde gebruikers (bijvoorbeeld een werknemer).",
                "3": "Black Box: De Pentester krijgt geen voorkennis van het doelsysteem dat wordt getest. Dus geen voorkennis van de interne werking, het architectuur OF de broncode. "
            }
        },
        "3": {
        "text": "Welke gebieden van uw beveiligingsinfrastructuur zijn momenteel het zwakst?",
        "options": {
            "1": "Externe netwerken",
            "2": "Interne netwerken",
            "3": "Cloudinfrastructuur",
            "4": "Bedrijfsapplicaties",
            "5": "Gebruikersaccountbeveiliging",
            "6": "Fysieke beveiliging van de faciliteit",
            "7": "Gegevensbeveiliging en encryptie",
            "8": "Beheer van leveranciersrisico's",
            "9": "Monitoring en rapportage van beveiligingsgebeurtenissen",
            "10": "Beveiliging van mobiele apparaten",
            "11": "Ik geef het liever niet aan"
            }
        },
        "4": {
            "text": "Heeft u al beveiligingsmaatregelen geïmplementeerd om deze zwakke punten aan te pakken?",
            "options": {
            "1": "Ja, we hebben maatregelen geïmplementeerd.",
            "2": "Nee, we hebben nog geen maatregelen geïmplementeerd, maar we zijn van plan dit te doen.",
            "3": "Nee, we hebben nog geen maatregelen geïmplementeerd en we hebben ook geen plannen om dit op korte termijn te doen.",
            "4": "We weten het niet zeker of onze huidige beveiligingsmaatregelen voldoende zijn om deze zwakke punten aan te pakken.",
            "5": "Ik geef het liever niet aan"
            }
        },
        "5": {
            "text": "Welke beveiligingsmaatregelen zou u willen implementeren na de pentest",
            "options": {
            "1": "Security Information and Event Management (SIEM)",
            "2": "Intrusion Detection System (IDS)",
            "3": "Intrusion Prevention System (IPS)",
            "4": "Data Encryption",
            "5": "Access Control",
            "6": "Multi-factor authentication",
            "7": "Security policies and procedures",
            "8": "Security awareness training",
            "9": "Regular penetration testing and vulnerability scanning",
            "10": "Network segmentation and isolation",
            "11": "Improved incident response and disaster recovery planning",
            "12": "Geef ik liever niet op"
            }
        },
        "6": {
            "text": "Hoe wilt u dat uw beveiligingsniveau eruit ziet na de pentest?",
            "options": {
            "1": "Een zo hoog mogelijk niveau van beveiliging, ongeacht de kosten.",
            "2": "Een hoog beveiligingsniveau, maar binnen een bepaald budget.",
            "3": "Een basis beveiligingsniveau om te voldoen aan de minimale vereisten.",
            "4": "Een beveiligingsniveau dat past bij de risico's die uw organisatie loopt.",
            "5": "Ik geef het liever niet aan"
            }
        },
    },
    "6" : {
        "1": {
            "text": "Welke systemen en netwerken wilt u laten testen? Selecteer de situatie die het beste bij u past:",
            "options": {
                "1": "Externe website: Een website die toegankelijk is vanuit het publieke internet.",
                "2": "Interne website: Een website die alleen toegankelijk is vanuit uw bedrijfsnetwerk.",
                "3": "Desktop software: Een desktopapplicatie die op uw bedrijfsnetwerk draait.",
                "4": "Mobiele applicatie: Een mobiele app die op iOS of Android draait.",
                "5": "Bedrijfsnetwerk: Een interne bedrijfsnetwerk met meerdere servers, computers en apparaten.",
                "6": "Medewerkers: Het bewustzijn van uw medewerkers testen met betrekking tot informatiebeveiliging.",
                "7": "Cloudinfrastructuur: Een cloudgebaseerde infrastructuur zoals AWS of Azure.",
                "8": "Extern netwerk: Een netwerk dat toegankelijk is vanaf het internet.",
                "9": "Interne netwerken: Interne bedrijfsnetwerken met meerdere servers, computers en apparaten.",
                "10": "Draadloze netwerken: Wifi-netwerken die toegankelijk zijn voor het publiek of binnen uw organisatie.",
                "11": "Internet of Things (IoT): Apparaten die met het internet zijn verbonden, zoals slimme thermostaten, beveiligingscamera's en slimme speakers."
            }
        },
        "2": {
            "text": "Welk pentestscenario past het beste bij uw behoeften? Selecteer de situatie die het beste bij u past:",
            "options": {
                "1": "White Box: De Pentester krijgt volledige kennis van het doelsysteem, inclusief de broncode en de architectuur van het systeem. ",
                "2": "Grey Box: De Pentester krijgt (beperkte) toegang tot de systeeminformatie die normaal gesproken beschikbaar is voor alleen geautoriseerde gebruikers (bijvoorbeeld een werknemer).",
                "3": "Black Box: De Pentester krijgt geen voorkennis van het doelsysteem dat wordt getest. Dus geen voorkennis van de interne werking, het architectuur OF de broncode. "
            }
        },
        "3": {
        "text": "Wat zijn de specifieke beveiligingsvereisten voor uw nieuwe systemen, applicaties of netwerken?",
        "options": {
            "1": "Gegevensversleuteling",
            "2": "Toegangscontrole en autorisatie",
            "3": "Authenticatie van gebruikers",
            "4": "Security monitoring",
            "5": "Regelmatige software-updates",
            "6": "Firewalls",
            "7": "Fysieke beveiliging van de apparatuur",
            "8": "Beperking van het aantal en de rechten van gebruikers",
            "9": "Regelmatige beoordelingen van de beveiligingsstatus",
            "10": "Ik geef het liever niet aan"
            }
        },
        "4": {
            "text": "Zijn er bepaalde beveiligingsrisico's waar u zich zorgen over maakt met betrekking tot deze nieuwe systemen, applicaties of netwerken?",
            "options": {
            "1": "Datalekken",
            "2": "Phishingaanvallen",
            "3": "Ransomware",
            "4": "Ongeautoriseerde toegang",
            "5": "DDoS-aanvallen",
            "6": "Malware",
            "7": "Insider bedreigingen",
            "8": "Onveilige webapplicaties",
            "9": "Slechte wachtwoordbeveiliging",
            "10": "Slecht beheerde netwerkapparatuur",
            "11": "Ik maak me geen zorgen",
            "12": "Geen van bovengenoemde maatregelen",
            "13": "Ik geef het liever niet aan"
            }
        },
        "5": {
            "text": "Welk tijdsbestek heeft u vastgesteld voor de uitvoering van de pentest?",
            "options": {
            "1": "Minder dan een maand",
            "2": "Minder dan drie maanden",
            "3": "Minder dan zes maanden",
            "4": "Meer dan zes maanden",
            "5": "Geen vastgesteld tijdsbestek"
            }
        },
        "6": {
            "text": "Heeft u al andere beveiligingsmaatregelen geïmplementeerd om deze nieuwe systemen, applicaties of netwerken te beveiligen?",
            "options": {
            "1": "Ja, we hebben maatregelen geïmplementeerd.",
            "2": "Nee, we hebben nog geen maatregelen geïmplementeerd, maar we zijn van plan dit te doen.",
            "3": "Nee, we hebben nog geen maatregelen geïmplementeerd en we hebben ook geen plannen om dit op korte termijn te doen.",
            "4": "We weten het niet zeker of onze huidige beveiligingsmaatregelen voldoende zijn om deze zwakke punten aan te pakken.",
            "5": "Ik geef het liever niet aan"
            }
        },
    },
    "7" : {
        "1": {
            "text": "Welke systemen en netwerken wilt u laten testen? Selecteer de situatie die het beste bij u past:",
            "options": {
                "1": "Externe website: Een website die toegankelijk is vanuit het publieke internet.",
                "2": "Interne website: Een website die alleen toegankelijk is vanuit uw bedrijfsnetwerk.",
                "3": "Desktop software: Een desktopapplicatie die op uw bedrijfsnetwerk draait.",
                "4": "Mobiele applicatie: Een mobiele app die op iOS of Android draait.",
                "5": "Bedrijfsnetwerk: Een interne bedrijfsnetwerk met meerdere servers, computers en apparaten.",
                "6": "Medewerkers: Het bewustzijn van uw medewerkers testen met betrekking tot informatiebeveiliging.",
                "7": "Cloudinfrastructuur: Een cloudgebaseerde infrastructuur zoals AWS of Azure.",
                "8": "Extern netwerk: Een netwerk dat toegankelijk is vanaf het internet.",
                "9": "Interne netwerken: Interne bedrijfsnetwerken met meerdere servers, computers en apparaten.",
                "10": "Draadloze netwerken: Wifi-netwerken die toegankelijk zijn voor het publiek of binnen uw organisatie.",
                "11": "Internet of Things (IoT): Apparaten die met het internet zijn verbonden, zoals slimme thermostaten, beveiligingscamera's en slimme speakers."
            }
        },
        "2": {
            "text": "Welk pentestscenario past het beste bij uw behoeften? Selecteer de situatie die het beste bij u past:",
            "options": {
                "1": "White Box: De Pentester krijgt volledige kennis van het doelsysteem, inclusief de broncode en de architectuur van het systeem. ",
                "2": "Grey Box: De Pentester krijgt (beperkte) toegang tot de systeeminformatie die normaal gesproken beschikbaar is voor alleen geautoriseerde gebruikers (bijvoorbeeld een werknemer).",
                "3": "Black Box: De Pentester krijgt geen voorkennis van het doelsysteem dat wordt getest. Dus geen voorkennis van de interne werking, het architectuur OF de broncode. "
            }
        },
        "3": {
        "text": "Welke specifieke beveiligingsmaatregelen zijn er geïmplementeerd voor uw personeel?",
        "options": {
            "1": "Ons personeel wordt verplicht om sterke wachtwoorden te gebruiken en deze regelmatig te wijzigen om de beveiliging te verbeteren. We hebben ook tweefactorauthenticatie geïmplementeerd voor toegang tot gevoelige systemen.",
            "2": "We bieden regelmatige trainingen aan ons personeel om hen bewust te maken van beveiligingsrisico's en hoe ze deze kunnen voorkomen. We hebben ook beveiligingsprocedures voor het werken met gevoelige informatie.",
            "3": "We hebben beveiligingscamera's en toegangscontrolesystemen geïnstalleerd in onze kantoren en faciliteiten om ongeautoriseerde toegang te voorkomen. Ons personeel is ook getraind in het herkennen van verdachte activiteiten en het rapporteren van incidenten.",
            "4": "We hebben firewalls en andere beveiligingsmaatregelen geïmplementeerd op onze netwerken om te voorkomen dat ongeautoriseerde toegang tot onze systemen plaatsvindt. Ons personeel is ook getraind in het herkennen van phishingaanvallen en andere vormen van kwaadaardige activiteit.",
            "5": "We hebben beleid en procedures geïmplementeerd om gevoelige informatie te beschermen en ervoor te zorgen dat deze alleen wordt gedeeld met geautoriseerde partijen. Ons personeel is getraind in het omgaan met gevoelige informatie en het voorkomen van onbedoelde lekken.",
            "6": "Ik geef het liever niet aan"
            }
        },
        "4": {
            "text": "Heeft u recentelijk beveiligingsincidenten meegemaakt als gevolg van personeelsveranderingen?",
            "options": {
            "1": "Ja",
            "2": "Nee",
            "3": "Ik geef het liever niet aan"
            }
        },
        "5": {
            "text": "Welke stappen heeft u genomen om de beveiliging te versterken na personeelsveranderingen?",
            "options": {
            "1": "Het resetten van wachtwoorden en toegangscodes voor voormalige medewerkers.",
            "2": "Het bijwerken van toegangscontroles en -bevoegdheden om de toegang tot gevoelige gegevens te beperken.",
            "3": "Het verstrekken van nieuwe toegangscodes en wachtwoorden aan nieuwe medewerkers.",
            "4": "Het verhogen van de frequentie van veiligheidstrainingen voor medewerkers om bewustzijn te creëren over beveiligingsrisico's en best practices.",
            "5": "Het uitvoeren van een grondige beoordeling van de beveiligingsmaatregelen na personeelsveranderingen om te identificeren waar er ruimte is voor verbetering en versterking van de beveiliging.",
            "6": "Ik geef het liever niet aan"
            }
        },
        "6": {
            "text": "Welke impact kan het niet uitvoeren van de pentest hebben op de beveiliging van uw personeel en bedrijfsgegevens?",
            "options": {
            "1": "Verlies van vertrouwen",
            "2": "Contractbreuk",
            "3": "Vertraging van projecten",
            "4": "Negatieve publiciteit",
            "5": "Financiële gevolgen",
            "6": "Ik geef het liever niet aan"
            }
        },
    },
    "8" : {
        "1": {
            "text": "Welke systemen en netwerken wilt u laten testen? Selecteer de situatie die het beste bij u past:",
            "options": {
                "1": "Externe website: Een website die toegankelijk is vanuit het publieke internet.",
                "2": "Interne website: Een website die alleen toegankelijk is vanuit uw bedrijfsnetwerk.",
                "3": "Desktop software: Een desktopapplicatie die op uw bedrijfsnetwerk draait.",
                "4": "Mobiele applicatie: Een mobiele app die op iOS of Android draait.",
                "5": "Bedrijfsnetwerk: Een interne bedrijfsnetwerk met meerdere servers, computers en apparaten.",
                "6": "Medewerkers: Het bewustzijn van uw medewerkers testen met betrekking tot informatiebeveiliging.",
                "7": "Cloudinfrastructuur: Een cloudgebaseerde infrastructuur zoals AWS of Azure.",
                "8": "Extern netwerk: Een netwerk dat toegankelijk is vanaf het internet.",
                "9": "Interne netwerken: Interne bedrijfsnetwerken met meerdere servers, computers en apparaten.",
                "10": "Draadloze netwerken: Wifi-netwerken die toegankelijk zijn voor het publiek of binnen uw organisatie.",
                "11": "Internet of Things (IoT): Apparaten die met het internet zijn verbonden, zoals slimme thermostaten, beveiligingscamera's en slimme speakers."
            }
        },
        "2": {
            "text": "Welk pentestscenario past het beste bij uw behoeften? Selecteer de situatie die het beste bij u past:",
            "options": {
                "1": "White Box: De Pentester krijgt volledige kennis van het doelsysteem, inclusief de broncode en de architectuur van het systeem. ",
                "2": "Grey Box: De Pentester krijgt (beperkte) toegang tot de systeeminformatie die normaal gesproken beschikbaar is voor alleen geautoriseerde gebruikers (bijvoorbeeld een werknemer).",
                "3": "Black Box: De Pentester krijgt geen voorkennis van het doelsysteem dat wordt getest. Dus geen voorkennis van de interne werking, het architectuur OF de broncode. "
            }
        },
        "3": {
        "text": "Welke specifieke beveiligingsvereisten heeft uw nieuwe klant of project?",
        "options": {
            "1": "ISO 27001",
            "2": "NEN7510",
            "3": "AVG/GDPR",
            "4": "HIPAA",
            "5": "PCI-DSS",
            "6": "SOX",
            "7": "FISMA",
            "8": "GLBA",
            "9": "CCPA",
            "10": "CMMC",
            "11": "NIST SP 800-171",
            "12": "EI3PA",
            "13": "SWIFT CSCF",
            "14": "CTPAT",
            "15": "ISO 20000-1",
            "16": "Geen van bovengenoemde",
            "17": "Ik geef het liever niet aan"
            }
        },
        "4": {
            "text": "Heeft uw nieuwe klant of project specifieke eisen voor de pentest?",
            "options": {
            "1": "Beperkte scope (alleen specifieke systemen)",
            "2": "Volledige scope (alle systemen)",
            "3": "Webapplicaties",
            "4": "Netwerk- en infrastructuurcomponenten",
            "5": "Andere (specificeer)",
            "5": "Ik geef het liever niet aan"
            }
        },
        "5": {
            "text": "Welk tijdsbestek heeft uw nieuwe klant of project vastgesteld voor de uitvoering van de pentest?",
            "options": {
            "1": "Binnen 1 maand",
            "2": "Binnen 3 maanden",
            "3": "Binnen 6 maanden",
            "4": "Binnen 1 jaar",
            "5": "Geen specifiek tijdsbestek",
            "6": "Ik geef het liever niet aan"
            }
        },
        "6": {
            "text": "Welke impact kan het niet uitvoeren van de pentest hebben op uw bedrijfsrelatie met uw nieuwe klant of project?",
            "options": {
            "1": "Contractbreuk",
            "2": "Financiële boetes",
            "3": "Verlies van vertrouwen",
            "4": "Schade aan de reputatie",
            "5": "Geen significante impact",
            "6": "Ik geef het liever niet aan"
            }
        },
    },
    "9" : {
        "1": {
            "text": "Welke systemen en netwerken wilt u laten testen? Selecteer de situatie die het beste bij u past:",
            "options": {
                "1": "Externe website: Een website die toegankelijk is vanuit het publieke internet.",
                "2": "Interne website: Een website die alleen toegankelijk is vanuit uw bedrijfsnetwerk.",
                "3": "Desktop software: Een desktopapplicatie die op uw bedrijfsnetwerk draait.",
                "4": "Mobiele applicatie: Een mobiele app die op iOS of Android draait.",
                "5": "Bedrijfsnetwerk: Een interne bedrijfsnetwerk met meerdere servers, computers en apparaten.",
                "6": "Medewerkers: Het bewustzijn van uw medewerkers testen met betrekking tot informatiebeveiliging.",
                "7": "Cloudinfrastructuur: Een cloudgebaseerde infrastructuur zoals AWS of Azure.",
                "8": "Extern netwerk: Een netwerk dat toegankelijk is vanaf het internet.",
                "9": "Interne netwerken: Interne bedrijfsnetwerken met meerdere servers, computers en apparaten.",
                "10": "Draadloze netwerken: Wifi-netwerken die toegankelijk zijn voor het publiek of binnen uw organisatie.",
                "11": "Internet of Things (IoT): Apparaten die met het internet zijn verbonden, zoals slimme thermostaten, beveiligingscamera's en slimme speakers."
            }
        },
        "2": {
            "text": "Welk pentestscenario past het beste bij uw behoeften? Selecteer de situatie die het beste bij u past:",
            "options": {
                "1": "White Box: De Pentester krijgt volledige kennis van het doelsysteem, inclusief de broncode en de architectuur van het systeem. ",
                "2": "Grey Box: De Pentester krijgt (beperkte) toegang tot de systeeminformatie die normaal gesproken beschikbaar is voor alleen geautoriseerde gebruikers (bijvoorbeeld een werknemer).",
                "3": "Black Box: De Pentester krijgt geen voorkennis van het doelsysteem dat wordt getest. Dus geen voorkennis van de interne werking, het architectuur OF de broncode. "
            }
        },
        "3": {
        "text": "Welke specifieke kwetsbaarheden heeft u geïdentificeerd?",
        "options": {
            "1": "Ongepatchte software",
            "2": "Onveilige configuraties",
            "3": "Zwakke wachtwoorden",
            "4": "Onveilige webapplicaties",
            "5": "Andere (specificeer)",
            "6": "Ik geef het liever niet aan"
            }
        },
        "4": {
            "text": "Heeft u eerder pogingen ondernomen om deze kwetsbaarheden aan te pakken?",
            "options": {
            "1": "Ja, met beperkt succes",
            "2": "Ja, maar zonder succes",
            "3": "Nee, we hebben hulp nodig om deze aan te pakken",
            "4": "Nee, we waren ons niet bewust van de kwetsbaarheden",
            "5": "Ik geef het liever niet aan"
            }
        },
        "5": {
            "text": "Welk tijdsbestek heeft u vastgesteld voor de uitvoering van de pentest?",
            "options": {
            "1": "Binnen 1 maand",
            "2": "Binnen 3 maanden",
            "3": "Binnen 6 maanden",
            "4": "Binnen 1 jaar",
            "5": "Geen specifiek tijdsbestek",
            "6": "Ik geef het liever niet aan"
            }
        },
        "6": {
            "text": "Welke impact kan het niet uitvoeren van de pentest hebben op uw bedrijfsgegevens en reputatie?",
            "options": {
            "1": "Datalekken",
            "2": "Verlies van klantgegevens",
            "3": "Schade aan de reputatie",
            "4": "Financiële schade",
            "5": "Andere (specificeer)",
            "6": "Ik geef het liever niet aan"
            }
        },
    },
}