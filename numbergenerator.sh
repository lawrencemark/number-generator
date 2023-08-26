#!/bin/bash
python3 phonenumbergen.py $1

case $1 in 

    UK|uk)

    toNumber="+44800123456"
    ;;

    FRANCE|France|france)

    toNumber="+33147777000"
    ;;

    GERMANY|Germany|germany)

    toNumber="+496997971000"
    ;;

    NETHERLANDS|Netherlands:netherlands)
    toNumber="+31205048000"
    ;;

    SPAIN|Spain|spain)
    toNumber="+34902375637"
    ;;

esac

sed "s/TONUMBER/$toNumber/g" sipp_uac_pcap_g711a.template > sipp_uac_invitewithrtp.xml

sudo sipp 192.168.244.128 -sf sipp_uac_invitewithrtp.xml -inf numbers.csv -r 3 -rp 30000 -l 250 -i 192.168.244.129


