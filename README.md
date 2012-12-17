## Voorbeelden PyQt college

Deze voorbeelden kun je uitvoeren op de LWP, nadat je het volgende
commando hebt uitgevoerd:

    export PYTHONPATH=/net/aps/64/lib/python3.1

Je kunt Qt Designer starten met:

    /net/aps/64/src/qt-everywhere-opensource-src-4.8.1/bin/designer

Als je pyuic4 wilt gebruiken, verander dan eerst het zoekpad:

    export PATH=/net/aps/64/opt/Python-3.1/bin:$PATH

Hierna kun je pyuic4 als volgt gebruiken:

    pyuic4 MijnWidget.ui > Ui_MijnWidget.py
