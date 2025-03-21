from django import template
from django.conf import settings
from django.utils.safestring import mark_safe

register = template.Library()

# Mapeo de valores de país a la ruta relativa del archivo en la carpeta media.
COUNTRY_FLAGS = {
    "af AFG": "banderas_paises/af.svg",
    "ax ALA": "banderas_paises/ax.svg",
    "al ALB": "banderas_paises/al.svg",
    "dz ALG": "banderas_paises/dz.svg",
    "as ASM": "banderas_paises/as.svg",
    "ad AND": "banderas_paises/ad.svg",
    "ao ANG": "banderas_paises/ao.svg",
    "ai AIA": "banderas_paises/ai.svg",
    "aq ATA": "banderas_paises/aq.svg",
    "ag ATG": "banderas_paises/ag.svg",
    "ar ARG": "banderas_paises/ar.svg",
    "am ARM": "banderas_paises/am.svg",
    "aw ABW": "banderas_paises/aw.svg",
    "au AUS": "banderas_paises/au.svg",
    "at AUT": "banderas_paises/at.svg",
    "az AZE": "banderas_paises/az.svg",
    "bs BHS": "banderas_paises/bs.svg",
    "bh BHR": "banderas_paises/bh.svg",
    "bd BGD": "banderas_paises/bd.svg",
    "bb BRB": "banderas_paises/bb.svg",
    "by BLR": "banderas_paises/by.svg",
    "be BEL": "banderas_paises/be.svg",
    "bz BLZ": "banderas_paises/bz.svg",
    "bj BEN": "banderas_paises/bj.svg",
    "bm BMU": "banderas_paises/bm.svg",
    "bt BTN": "banderas_paises/bt.svg",
    "bo BOL": "banderas_paises/bo.svg",
    "bq BES": "banderas_paises/bq.svg",
    "ba BIH": "banderas_paises/ba.svg",
    "bw BWA": "banderas_paises/bw.svg",
    "bv BVT": "banderas_paises/bv.svg",
    "br BRA": "banderas_paises/br.svg",
    "io IOT": "banderas_paises/io.svg",
    "bn BRN": "banderas_paises/bn.svg",
    "bg BGR": "banderas_paises/bg.svg",
    "bf BFA": "banderas_paises/bf.svg",
    "bi BDI": "banderas_paises/bi.svg",
    "kh KHM": "banderas_paises/kh.svg",
    "cm CMR": "banderas_paises/cm.svg",
    "ca CAN": "banderas_paises/ca.svg",
    "cv CPV": "banderas_paises/cv.svg",
    "ky CYM": "banderas_paises/ky.svg",
    "cf CAF": "banderas_paises/cf.svg",
    "td TCD": "banderas_paises/td.svg",
    "cl CHI": "banderas_paises/cl.svg",
    "cn CHN": "banderas_paises/cn.svg",
    "cx CXR": "banderas_paises/cx.svg",
    "cc CCK": "banderas_paises/cc.svg",
    "co COL": "banderas_paises/co.svg",
    "km COM": "banderas_paises/km.svg",
    "cg CGO": "banderas_paises/cg.svg",
    "cd COD": "banderas_paises/cd.svg",
    "ck COK": "banderas_paises/ck.svg",
    "cr CRI": "banderas_paises/cr.svg",
    "ci CIV": "banderas_paises/ci.svg",
    "hr CRO": "banderas_paises/hr.svg",
    "cu CUB": "banderas_paises/cu.svg",
    "cw CUW": "banderas_paises/cw.svg",
    "cy CYP": "banderas_paises/cy.svg",
    "cz CZE": "banderas_paises/cz.svg",
    "dk DEN": "banderas_paises/dk.svg",
    "dj DJI": "banderas_paises/dj.svg",
    "dm DMA": "banderas_paises/dm.svg",
    "do DOM": "banderas_paises/do.svg",
    "ec ECU": "banderas_paises/ec.svg",
    "eg EGY": "banderas_paises/eg.svg",
    "sv SLV": "banderas_paises/sv.svg",
    "gq EQG": "banderas_paises/gq.svg",
    "er ERI": "banderas_paises/er.svg",
    "ee EST": "banderas_paises/ee.svg",
    "et ETH": "banderas_paises/et.svg",
    "fk FLK": "banderas_paises/fk.svg",
    "fo FRO": "banderas_paises/fo.svg",
    "fj FJI": "banderas_paises/fj.svg",
    "fi FIN": "banderas_paises/fi.svg",
    "fr FRA": "banderas_paises/fr.svg",
    "gf GUF": "banderas_paises/gf.svg",
    "py PAR": "banderas_paises/pf.svg",
    "tf ATF": "banderas_paises/tf.svg",
    "ga GAB": "banderas_paises/ga.svg",
    "gm GMB": "banderas_paises/gm.svg",
    "ge GEO": "banderas_paises/ge.svg",
    "de GER": "banderas_paises/de.svg",
    "gh GHA": "banderas_paises/gh.svg",
    "gi GIB": "banderas_paises/gi.svg",
    "gr GRE": "banderas_paises/gr.svg",
    "gl GRL": "banderas_paises/gl.svg",
    "gd GRD": "banderas_paises/gd.svg",
    "gp GLP": "banderas_paises/gp.svg",
    "gu GUM": "banderas_paises/gu.svg",
    "gt GTM": "banderas_paises/gt.svg",
    "gg GGY": "banderas_paises/gg.svg",
    "gn GIN": "banderas_paises/gn.svg",
    "gw GNB": "banderas_paises/gw.svg",
    "gy GUY": "banderas_paises/gy.svg",
    "ht HTI": "banderas_paises/ht.svg",
    "hm HMD": "banderas_paises/hm.svg",
    "va VAT": "banderas_paises/va.svg",
    "hn HND": "banderas_paises/hn.svg",
    "hk HKG": "banderas_paises/hk.svg",
    "hu HUN": "banderas_paises/hu.svg",
    "is ISL": "banderas_paises/is.svg",
    "in IND": "banderas_paises/in.svg",
    "id IDN": "banderas_paises/id.svg",
    "ir IRN": "banderas_paises/ir.svg",
    "iq IRQ": "banderas_paises/iq.svg",
    "ie IRL": "banderas_paises/ie.svg",
    "im IMN": "banderas_paises/im.svg",
    "il ISR": "banderas_paises/il.svg",
    "it ITA": "banderas_paises/it.svg",
    "jm JAM": "banderas_paises/jm.svg",
    "jp JPN": "banderas_paises/jp.svg",
    "je JEY": "banderas_paises/je.svg",
    "jo JOR": "banderas_paises/jo.svg",
    "kz KAZ": "banderas_paises/kz.svg",
    "ke KEN": "banderas_paises/ke.svg",
    "ki KIR": "banderas_paises/ki.svg",
    "kp PRK": "banderas_paises/kp.svg",
    "kr KOR": "banderas_paises/kr.svg",
    "kw KWT": "banderas_paises/kw.svg",
    "kg KGZ": "banderas_paises/kg.svg",
    "la LAO": "banderas_paises/la.svg",
    "lv LVA": "banderas_paises/lv.svg",
    "lb LBN": "banderas_paises/lb.svg",
    "ls LSO": "banderas_paises/ls.svg",
    "lr LBR": "banderas_paises/lr.svg",
    "ly LBY": "banderas_paises/ly.svg",
    "li LIE": "banderas_paises/li.svg",
    "lt LTU": "banderas_paises/lt.svg",
    "xk KVX": "banderas_paises/lu.svg",
    "mo MAC": "banderas_paises/mo.svg",
    "mk MKD": "banderas_paises/mk.svg",
    "mg MDG": "banderas_paises/mg.svg",
    "mw MWI": "banderas_paises/mw.svg",
    "my MYS": "banderas_paises/my.svg",
    "mv MDV": "banderas_paises/mv.svg",
    "ml MLI": "banderas_paises/ml.svg",
    "mt MLT": "banderas_paises/mt.svg",
    "mh MHL": "banderas_paises/mh.svg",
    "mq MTQ": "banderas_paises/mq.svg",
    "mr MRT": "banderas_paises/mr.svg",
    "mu MUS": "banderas_paises/mu.svg",
    "yt MYT": "banderas_paises/yt.svg",
    "mx MEX": "banderas_paises/mx.svg",
    "fm FSM": "banderas_paises/fm.svg",
    "md MDA": "banderas_paises/md.svg",
    "mc MCO": "banderas_paises/mc.svg",
    "mn MNG": "banderas_paises/mn.svg",
    "me MNE": "banderas_paises/me.svg",
    "ms MSR": "banderas_paises/ms.svg",
    "ma MAR": "banderas_paises/ma.svg",
    "mz MOZ": "banderas_paises/mz.svg",
    "mm MMR": "banderas_paises/mm.svg",
    "na NAM": "banderas_paises/na.svg",
    "nr NRU": "banderas_paises/nr.svg",
    "np NPL": "banderas_paises/np.svg",
    "nl NED": "banderas_paises/nl.svg",
    "nc NCL": "banderas_paises/nc.svg",
    "nz NZL": "banderas_paises/nz.svg",
    "ni NIC": "banderas_paises/ni.svg",
    "ne NER": "banderas_paises/ne.svg",
    "ng NGA": "banderas_paises/ng.svg",
    "nu NIU": "banderas_paises/nu.svg",
    "nf NFK": "banderas_paises/nf.svg",
    "mp MNP": "banderas_paises/mp.svg",
    "no NOR": "banderas_paises/no.svg",
    "om OMN": "banderas_paises/om.svg",
    "pk PAK": "banderas_paises/pk.svg",
    "pw PLW": "banderas_paises/pw.svg",
    "ps PSE": "banderas_paises/ps.svg",
    "pa PAN": "banderas_paises/pa.svg",
    "pg PNG": "banderas_paises/pg.svg",
    "py PRY": "banderas_paises/py.svg",
    "pe PER": "banderas_paises/pe.svg",
    "ph PHL": "banderas_paises/ph.svg",
    "pn PCN": "banderas_paises/pn.svg",
    "pl POL": "banderas_paises/pl.svg",
    "pt POR": "banderas_paises/pt.svg",
    "pr PRI": "banderas_paises/pr.svg",
    "qa QAT": "banderas_paises/qa.svg",
    "re REU": "banderas_paises/re.svg",
    "ro ROU": "banderas_paises/ro.svg",
    "ru RUS": "banderas_paises/ru.svg",
    "rw RWA": "banderas_paises/rw.svg",
    "bl BLM": "banderas_paises/bl.svg",
    "sh SHN": "banderas_paises/sh.svg",
    "kn KNA": "banderas_paises/kn.svg",
    "lc LCA": "banderas_paises/lc.svg",
    "mf MAF": "banderas_paises/maf.svg",
    "pm SPM": "banderas_paises/spm.svg",
    "vc VCT": "banderas_paises/vc.svg",
    "ws WSM": "banderas_paises/ws.svg",
    "sm SMR": "banderas_paises/sm.svg",
    "st STP": "banderas_paises/st.svg",
    "sa KSA": "banderas_paises/sa.svg",
    "sn SEN": "banderas_paises/sn.svg",
    "rs SRB": "banderas_paises/rs.svg",
    "sct SCO": "banderas_paises/sc.svg",
    "sl SLE": "banderas_paises/sl.svg",
    "sg SGP": "banderas_paises/sg.svg",
    "sx SXM": "banderas_paises/sx.svg",
    "sk SVK": "banderas_paises/sk.svg",
    "si SVN": "banderas_paises/si.svg",
    "sb SLB": "banderas_paises/sb.svg",
    "so SOM": "banderas_paises/so.svg",
    "za ZAF": "banderas_paises/za.svg",
    "gs SGS": "banderas_paises/gs.svg",
    "ss SSD": "banderas_paises/ss.svg",
    "es ESP": "banderas_paises/es.svg",
    "lk LKA": "banderas_paises/lk.svg",
    "sd SDN": "banderas_paises/sd.svg",
    "sr SUR": "banderas_paises/sr.svg",
    "sj SJM": "banderas_paises/sj.svg",
    "sz SWZ": "banderas_paises/sz.svg",
    "se SWE": "banderas_paises/se.svg",
    "ch CHE": "banderas_paises/ch.svg",
    "sy SYR": "banderas_paises/sy.svg",
    "tw TWN": "banderas_paises/tw.svg",
    "tj TJK": "banderas_paises/tj.svg",
    "tz TZA": "banderas_paises/tz.svg",
    "th THA": "banderas_paises/th.svg",
    "tl TLS": "banderas_paises/tl.svg",
    "tg TOG": "banderas_paises/tg.svg",
    "tk TKL": "banderas_paises/tk.svg",
    "to TON": "banderas_paises/to.svg",
    "tt TTO": "banderas_paises/tt.svg",
    "tn TUN": "banderas_paises/tn.svg",
    "tr TUR": "banderas_paises/tr.svg",
    "tm TKM": "banderas_paises/tm.svg",
    "tc TCA": "banderas_paises/tc.svg",
    "tv TUV": "banderas_paises/tv.svg",
    "ug UGA": "banderas_paises/ug.svg",
    "ua UKR": "banderas_paises/ua.svg",
    "ae ARE": "banderas_paises/ae.svg",
    "gb GBR": "banderas_paises/gb.svg",
    "us USA": "banderas_paises/us.svg",
    "um UMI": "banderas_paises/um.svg",
    "uy URU": "banderas_paises/uy.svg",
    "uz UZB": "banderas_paises/uz.svg",
    "vu VUT": "banderas_paises/vu.svg",
    "ve VEN": "banderas_paises/ve.svg",
    "vn VNM": "banderas_paises/vn.svg",
    "vg VGB": "banderas_paises/vg.svg",
    "vi VIR": "banderas_paises/vi.svg",
    "eng ENG": "banderas_paises/gb-eng.svg",
    "ch SUI": "banderas_paises/gl.svg",
    "zm ZAM": "banderas_paises/zm.svg",
    "zw ZIM": "banderas_paises/zw.svg",
}

@register.filter
def flag(country_str):
    """
    Devuelve una etiqueta <img> con la bandera si existe en el mapeo,
    de lo contrario, devuelve el mismo valor de country_str.
    """
    file_path = COUNTRY_FLAGS.get(country_str)
    if file_path:
        url = f"{settings.MEDIA_URL}{file_path}"
        return mark_safe(f'<img src="{url}" alt="{country_str}" style="width:30px; height:auto;">')
    return country_str