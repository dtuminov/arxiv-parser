# Parser for arXiv
import logging

from get_url_list import get_url_list
from get_xml import get_xml
from get_json import get_json
import xml.etree.ElementTree as ET

# Настройка логгирования
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Список возможных категорий для arXiv.
categories = [
    'cs.AI', 'cs.AR', 'cs.CC', 'cs.CE', 'cs.CG', 'cs.CL', 'cs.CR', 'cs.CV', 'cs.CY', 'cs.DB', 'cs.DC', 'cs.DL', 'cs.DM',
    'cs.DS', 'cs.ET', 'cs.FL', 'cs.GL', 'cs.GR', 'cs.GT', 'cs.HC', 'cs.IR', 'cs.IT', 'cs.LG', 'cs.LO', 'cs.MA', 'cs.MM',
    'cs.MS', 'cs.NA', 'cs.NE', 'cs.NI', 'cs.OH', 'cs.OS', 'cs.PF', 'cs.PL', 'cs.RO', 'cs.SC', 'cs.SD', 'cs.SE', 'cs.SI',
    'cs.SY',
    'econ.EM', 'econ.GN', 'econ.TH',
    'eess.AS', 'eess.IV', 'eess.SP', 'eess.SY',
    'math.AC', 'math.AG', 'math.AP', 'math.AT', 'math.CA', 'math.CO', 'math.CT', 'math.CV', 'math.DG', 'math.DS',
    'math.FA', 'math.GM', 'math.GN', 'math.GR', 'math.GT', 'math.HO', 'math.IT', 'math.KT', 'math.LO', 'math.MG',
    'math.MP', 'math.NA', 'math.NT', 'math.OA', 'math.OC', 'math.PR', 'math.QA', 'math.RA', 'math.RT', 'math.SG',
    'math.SP', 'math.ST',
    'q-bio.BM', 'q-bio.CB', 'q-bio.GN', 'q-bio.MN', 'q-bio.NC', 'q-bio.OT', 'q-bio.PE', 'q-bio.QM',
    'q-bio.SC', 'q-bio.TO',
    'q-fin.CP', 'q-fin.EC', 'q-fin.GN', 'q-fin.MF', 'q-fin.PM', 'q-fin.PR', 'q-fin.RM', 'q-fin.ST', 'q-fin.TR',
    'stat.AP', 'stat.CO', 'stat.ME', 'stat.ML', 'stat.OT', 'stat.TH'
]

# data_start и data_range — параметры нумерации страниц.
data_start = 0
data_range = 10

#  Будет выполнен поиск по всем статьям категорий.

if __name__ == '__main__':
    print('Building URL list...')
    url_list = get_url_list(categories, data_start, data_range)
    print('Pinging API...')
    xml_list = get_xml(url_list)
    print('Saving JSON files...')
    _ = get_json(xml_list)
    print('Done!')
