# coding=utf-8
"""Common functionality used by regression tests
"""

import numpy
import os
import sys
import logging
from numpy.testing import Tester

from safe.common.numerics import axes_to_points
from safe.common.version import get_version


LOGGER = logging.getLogger('InaSAFE')
QGIS_APP = None  # Static variable used to hold hand to running QGIS app
CANVAS = None
PARENT = None
IFACE = None


class SafeTester(Tester):
    """Tester class for testing SAFE package."""
    def _show_system_info(self):
        print 'safe version %s' % get_version()
        super(SafeTester, self)._show_system_info()


# usage: >>> from safe.common.testing import test_safe
#        >>> test_safe()
test_safe = SafeTester().test

# Find parent parent directory to path
# NOTE: This must match Makefile target testdata
# FIXME (Ole): Use environment variable for this.
# Assuming test data three lvls up
pardir = os.path.abspath(os.path.join(os.path.realpath(os.path.dirname(
    __file__)),
    '..',
    '..',
    '..'))

# Location of test data
DATANAME = 'inasafe_data'
DATADIR = os.path.join(pardir, DATANAME)

# Bundled test data
TESTDATA = os.path.join(DATADIR, 'test')  # Artificial datasets
HAZDATA = os.path.join(DATADIR, 'hazard')  # Real hazard layers
EXPDATA = os.path.join(DATADIR, 'exposure')  # Real exposure layers
BOUNDDATA = os.path.join(DATADIR, 'boundaries')  # Real exposure layers

UNITDATA = os.path.abspath(
    os.path.join(os.path.dirname(__file__),
                 '..',
                 'test',
                 'data'))

# Known feature counts in test data
FEATURE_COUNTS = {
    'test_buildings.shp': 144,
    'tsunami_building_exposure.shp': 19,
    'kecamatan_geo.shp': 42,
    'Padang_WGS84.shp': 3896,
    'OSM_building_polygons_20110905.shp': 34960,
    'indonesia_highway_sample.shp': 2,
    'OSM_subset.shp': 79,
    'kecamatan_jakarta_osm.shp': 47}

# For testing of storage modules
GEOTRANSFORMS = [(105.3000035, 0.008333, 0.0, -5.5667785, 0.0, -0.008333),
                 (105.29857, 0.0112, 0.0, -5.565233000000001, 0.0, -0.0112),
                 (96.956, 0.03074106, 0.0, 2.2894972560001, 0.0, -0.03074106)]


def combine_coordinates(x, y):
    """Make list of all combinations of points for x and y coordinates
    :param x:
    :param y:
    """

    return axes_to_points(x, y)


# For polygon testing
test_lines = [numpy.array([[122.231021, -8.626557],
                           [122.230563, -8.626194],
                           [122.228790, -8.624855],
                           [122.227536, -8.624059],
                           [122.226648, -8.623494],
                           [122.225775, -8.623022],
                           [122.224872, -8.622444],
                           [122.224230, -8.622100],
                           [122.221931, -8.621082],
                           [122.221700, -8.620980],
                           [122.220577, -8.620555],
                           [122.219580, -8.621030]]),
              numpy.array([[122.231621, -8.626837],
                           [122.231221, -8.628815],
                           [122.230381, -8.633296],
                           [122.229211, -8.639560],
                           [122.228404, -8.643688],
                           [122.228340, -8.643792],
                           [122.228330, -8.644103],
                           [122.226939, -8.651254],
                           [122.226158, -8.655796],
                           [122.226085, -8.656345],
                           [122.226098, -8.658629],
                           [122.226220, -8.659293],
                           [122.226251, -8.659496],
                           [122.226331, -8.659609],
                           [122.226324, -8.659723],
                           [122.226213, -8.659857],
                           [122.226136, -8.660063],
                           [122.226192, -8.660974],
                           [122.226279, -8.661290],
                           [122.226331, -8.661902]]),
              numpy.array([[122.226889, -8.625599],
                           [122.227299, -8.624500],
                           [122.227409, -8.624221],
                           [122.227536, -8.624059]]),
              numpy.array([[122.237129, -8.628637],
                           [122.233170, -8.627332],
                           [122.231621, -8.626837],
                           [122.231021, -8.626557]]),
              numpy.array([[122.237129, -8.628637],
                           [122.237302, -8.628694],
                           [122.238308, -8.629055],
                           [122.239825, -8.629696],
                           [122.241483, -8.630410],
                           [122.244142, -8.631634],
                           [122.244682, -8.631817],
                           [122.245104, -8.631978],
                           [122.245178, -8.631995],
                           [122.245259, -8.632025],
                           [122.245333, -8.632046],
                           [122.245474, -8.632101],
                           [122.246997, -8.632655],
                           [122.247938, -8.632926],
                           [122.248294, -8.633040],
                           [122.251185, -8.633644],
                           [122.255205, -8.634337],
                           [122.257082, -8.634719],
                           [122.258420, -8.634980],
                           [122.262063, -8.636138],
                           [122.263548, -8.636398]]),
              numpy.array([[122.247938, -8.632926],
                           [122.247940, -8.633560],
                           [122.247390, -8.636220]])]


test_polygon = numpy.array([[122.229086, -8.624406],
                            [122.229165, -8.624428],
                            [122.229339, -8.624562],
                            [122.229358, -8.624588],
                            [122.229329, -8.624656],
                            [122.229447, -8.624836],
                            [122.229646, -8.624878],
                            [122.229722, -8.624769],
                            [122.229872, -8.624858],
                            [122.230035, -8.625277],
                            [122.230333, -8.625382],
                            [122.231016, -8.625562],
                            [122.231332, -8.625655],
                            [122.231515, -8.625699],
                            [122.231695, -8.625837],
                            [122.231878, -8.625971],
                            [122.232058, -8.626109],
                            [122.232221, -8.626160],
                            [122.232834, -8.626485],
                            [122.233179, -8.626606],
                            [122.233422, -8.626652],
                            [122.233715, -8.626755],
                            [122.234381, -8.626836],
                            [122.234646, -8.627018],
                            [122.235011, -8.627153],
                            [122.235323, -8.627281],
                            [122.235964, -8.627383],
                            [122.237428, -8.627456],
                            [122.237692, -8.627611],
                            [122.237859, -8.627791],
                            [122.238087, -8.627801],
                            [122.238252, -8.627715],
                            [122.238644, -8.627886],
                            [122.238918, -8.627930],
                            [122.239374, -8.628171],
                            [122.239722, -8.628293],
                            [122.240053, -8.628339],
                            [122.240434, -8.628505],
                            [122.240858, -8.628607],
                            [122.241096, -8.628704],
                            [122.241549, -8.628792],
                            [122.241604, -8.628851],
                            [122.242095, -8.629023],
                            [122.242490, -8.629086],
                            [122.242734, -8.629202],
                            [122.242857, -8.629334],
                            [122.243557, -8.629650],
                            [122.244487, -8.630012],
                            [122.244684, -8.630157],
                            [122.244764, -8.630243],
                            [122.245091, -8.630386],
                            [122.245411, -8.630520],
                            [122.245551, -8.630617],
                            [122.245957, -8.630746],
                            [122.246591, -8.630968],
                            [122.246978, -8.631042],
                            [122.247375, -8.631182],
                            [122.247724, -8.631273],
                            [122.248289, -8.631364],
                            [122.248534, -8.631442],
                            [122.248998, -8.631703],
                            [122.249020, -8.631727],
                            [122.249043, -8.631784],
                            [122.249065, -8.631727],
                            [122.249315, -8.631930],
                            [122.249687, -8.632251],
                            [122.249938, -8.632380],
                            [122.250183, -8.632477],
                            [122.250599, -8.632758],
                            [122.251161, -8.633002],
                            [122.251689, -8.633155],
                            [122.253039, -8.633205],
                            [122.253888, -8.633189],
                            [122.254651, -8.633301],
                            [122.254932, -8.633296],
                            [122.255220, -8.633344],
                            [122.255778, -8.633469],
                            [122.256583, -8.633527],
                            [122.256945, -8.633574],
                            [122.257386, -8.633628],
                            [122.257629, -8.633712],
                            [122.258273, -8.633700],
                            [122.258945, -8.633803],
                            [122.259535, -8.633895],
                            [122.260058, -8.633964],
                            [122.260098, -8.634105],
                            [122.260751, -8.634187],
                            [122.260807, -8.634119],
                            [122.260941, -8.634198],
                            [122.260967, -8.634056],
                            [122.261675, -8.634076],
                            [122.261784, -8.634103],
                            [122.261752, -8.634246],
                            [122.262216, -8.634304],
                            [122.262752, -8.634239],
                            [122.262953, -8.634316],
                            [122.263125, -8.634295],
                            [122.263331, -8.634321],
                            [122.263486, -8.634262],
                            [122.263854, -8.634222],
                            [122.263975, -8.634152],
                            [122.264441, -8.634066],
                            [122.264822, -8.634019],
                            [122.264985, -8.634115],
                            [122.265569, -8.634016],
                            [122.265655, -8.633909],
                            [122.265900, -8.633819],
                            [122.266047, -8.633733],
                            [122.266205, -8.633714],
                            [122.266412, -8.633773],
                            [122.266486, -8.633867],
                            [122.266602, -8.633841],
                            [122.266624, -8.634173],
                            [122.266746, -8.634375],
                            [122.267067, -8.634570],
                            [122.267100, -8.634611],
                            [122.266940, -8.634589],
                            [122.266506, -8.634472],
                            [122.266434, -8.634552],
                            [122.266141, -8.634737],
                            [122.265576, -8.634900],
                            [122.265293, -8.635074],
                            [122.264771, -8.635224],
                            [122.264533, -8.635353],
                            [122.264439, -8.635396],
                            [122.264305, -8.635488],
                            [122.264075, -8.635531],
                            [122.263850, -8.635623],
                            [122.263695, -8.635671],
                            [122.263532, -8.635758],
                            [122.263428, -8.635805],
                            [122.263349, -8.635800],
                            [122.263225, -8.635807],
                            [122.263081, -8.636119],
                            [122.262723, -8.636165],
                            [122.262667, -8.636344],
                            [122.262500, -8.636420],
                            [122.262606, -8.636129],
                            [122.262302, -8.636072],
                            [122.262123, -8.636024],
                            [122.261711, -8.635936],
                            [122.261578, -8.635887],
                            [122.261394, -8.635844],
                            [122.261142, -8.635708],
                            [122.261079, -8.635570],
                            [122.261027, -8.635474],
                            [122.260890, -8.635482],
                            [122.260704, -8.635189],
                            [122.260769, -8.635009],
                            [122.260636, -8.634939],
                            [122.260575, -8.635134],
                            [122.260584, -8.635292],
                            [122.260432, -8.635524],
                            [122.260446, -8.635300],
                            [122.260349, -8.635214],
                            [122.260352, -8.635163],
                            [122.260342, -8.634988],
                            [122.260398, -8.634938],
                            [122.260484, -8.634843],
                            [122.260360, -8.634712],
                            [122.260125, -8.634893],
                            [122.259944, -8.634844],
                            [122.259594, -8.634801],
                            [122.259395, -8.634939],
                            [122.259223, -8.634928],
                            [122.259126, -8.634981],
                            [122.258842, -8.635067],
                            [122.257969, -8.634928],
                            [122.257808, -8.634840],
                            [122.257503, -8.634769],
                            [122.257399, -8.634653],
                            [122.257144, -8.634668],
                            [122.256916, -8.634586],
                            [122.257000, -8.634819],
                            [122.256986, -8.635038],
                            [122.256734, -8.634947],
                            [122.256032, -8.635039],
                            [122.255897, -8.635111],
                            [122.255625, -8.634879],
                            [122.255549, -8.635121],
                            [122.255489, -8.635566],
                            [122.255353, -8.635695],
                            [122.255294, -8.634918],
                            [122.255026, -8.634592],
                            [122.254568, -8.634429],
                            [122.254445, -8.634566],
                            [122.254260, -8.634312],
                            [122.253832, -8.634387],
                            [122.253717, -8.634380],
                            [122.253618, -8.634433],
                            [122.253522, -8.634641],
                            [122.253321, -8.634325],
                            [122.253059, -8.634340],
                            [122.252711, -8.634319],
                            [122.252361, -8.634561],
                            [122.252303, -8.634558],
                            [122.252220, -8.634377],
                            [122.252168, -8.634281],
                            [122.251893, -8.634196],
                            [122.251768, -8.634057],
                            [122.251675, -8.634107],
                            [122.251622, -8.634104],
                            [122.251522, -8.633887],
                            [122.250855, -8.633925],
                            [122.250689, -8.633865],
                            [122.250538, -8.633970],
                            [122.250438, -8.633916],
                            [122.250358, -8.633740],
                            [122.250274, -8.633697],
                            [122.250176, -8.634014],
                            [122.250018, -8.634367],
                            [122.249832, -8.634532],
                            [122.249790, -8.634090],
                            [122.249897, -8.633898],
                            [122.249582, -8.633923],
                            [122.249446, -8.633826],
                            [122.249403, -8.634058],
                            [122.249312, -8.634100],
                            [122.249086, -8.633692],
                            [122.248960, -8.633650],
                            [122.248858, -8.633876],
                            [122.248809, -8.633963],
                            [122.248788, -8.634032],
                            [122.248763, -8.634012],
                            [122.248722, -8.633724],
                            [122.248583, -8.633741],
                            [122.248405, -8.633600],
                            [122.248082, -8.633559],
                            [122.247800, -8.633478],
                            [122.247336, -8.633419],
                            [122.247225, -8.633235],
                            [122.247038, -8.633195],
                            [122.246992, -8.633086],
                            [122.246902, -8.633014],
                            [122.246862, -8.632873],
                            [122.246776, -8.632804],
                            [122.246701, -8.632980],
                            [122.246503, -8.633289],
                            [122.246444, -8.633491],
                            [122.246463, -8.633643],
                            [122.246444, -8.633792],
                            [122.246227, -8.633882],
                            [122.246170, -8.634078],
                            [122.246181, -8.634167],
                            [122.245977, -8.634444],
                            [122.245717, -8.634589],
                            [122.245479, -8.634788],
                            [122.245379, -8.634749],
                            [122.245398, -8.634678],
                            [122.245468, -8.634568],
                            [122.245633, -8.634505],
                            [122.245754, -8.634337],
                            [122.245808, -8.634136],
                            [122.245861, -8.634098],
                            [122.245899, -8.633774],
                            [122.245953, -8.633646],
                            [122.246014, -8.633346],
                            [122.246329, -8.633236],
                            [122.246401, -8.633052],
                            [122.246508, -8.632913],
                            [122.246491, -8.632828],
                            [122.246620, -8.632626],
                            [122.246773, -8.632517],
                            [122.246811, -8.632434],
                            [122.246675, -8.632336],
                            [122.246637, -8.632270],
                            [122.246837, -8.632194],
                            [122.246950, -8.632037],
                            [122.246994, -8.631904],
                            [122.246876, -8.631820],
                            [122.246695, -8.631934],
                            [122.246330, -8.631846],
                            [122.246098, -8.631891],
                            [122.245996, -8.631826],
                            [122.245956, -8.631925],
                            [122.246183, -8.632056],
                            [122.246202, -8.632128],
                            [122.246096, -8.632167],
                            [122.245757, -8.632132],
                            [122.245793, -8.632489],
                            [122.245494, -8.632599],
                            [122.245368, -8.632671],
                            [122.245314, -8.632546],
                            [122.245131, -8.632467],
                            [122.245037, -8.632354],
                            [122.244688, -8.632389],
                            [122.244454, -8.632556],
                            [122.244147, -8.632597],
                            [122.244082, -8.632231],
                            [122.243829, -8.632148],
                            [122.243583, -8.632288],
                            [122.243409, -8.632188],
                            [122.243267, -8.632202],
                            [122.243281, -8.632068],
                            [122.243087, -8.632011],
                            [122.243041, -8.631904],
                            [122.242918, -8.631802],
                            [122.242563, -8.631723],
                            [122.242394, -8.631740],
                            [122.242272, -8.631885],
                            [122.242221, -8.631653],
                            [122.242094, -8.631466],
                            [122.241680, -8.631641],
                            [122.241366, -8.631585],
                            [122.241457, -8.631510],
                            [122.241498, -8.631230],
                            [122.241386, -8.631241],
                            [122.241273, -8.631377],
                            [122.241144, -8.631222],
                            [122.240957, -8.631328],
                            [122.240887, -8.631349],
                            [122.240864, -8.630971],
                            [122.240319, -8.631014],
                            [122.240194, -8.631004],
                            [122.240073, -8.630733],
                            [122.240000, -8.630602],
                            [122.239959, -8.630418],
                            [122.239851, -8.630370],
                            [122.239692, -8.630383],
                            [122.239550, -8.630281],
                            [122.239383, -8.630294],
                            [122.239251, -8.630221],
                            [122.239386, -8.629779],
                            [122.239163, -8.629839],
                            [122.239024, -8.629999],
                            [122.238960, -8.629774],
                            [122.239059, -8.629690],
                            [122.239187, -8.629700],
                            [122.239230, -8.629557],
                            [122.239318, -8.629401],
                            [122.239231, -8.629244],
                            [122.239210, -8.629175],
                            [122.239317, -8.629143],
                            [122.239413, -8.628840],
                            [122.239152, -8.628472],
                            [122.239023, -8.628361],
                            [122.238880, -8.628526],
                            [122.238826, -8.628701],
                            [122.238723, -8.628742],
                            [122.238560, -8.628553],
                            [122.238340, -8.628570],
                            [122.238182, -8.628512],
                            [122.238054, -8.628522],
                            [122.237967, -8.628421],
                            [122.237778, -8.628337],
                            [122.237559, -8.628166],
                            [122.237122, -8.628085],
                            [122.237106, -8.628030],
                            [122.237066, -8.628070],
                            [122.237122, -8.628085],
                            [122.237157, -8.628180],
                            [122.236987, -8.628375],
                            [122.236899, -8.628382],
                            [122.236759, -8.628159],
                            [122.236625, -8.628314],
                            [122.236551, -8.628377],
                            [122.236571, -8.628625],
                            [122.236507, -8.628698],
                            [122.236372, -8.628602],
                            [122.236239, -8.628612],
                            [122.236173, -8.628370],
                            [122.236279, -8.628084],
                            [122.236212, -8.627972],
                            [122.236075, -8.628144],
                            [122.236105, -8.628527],
                            [122.235835, -8.628676],
                            [122.235764, -8.628516],
                            [122.235689, -8.628510],
                            [122.235461, -8.628528],
                            [122.235349, -8.628398],
                            [122.235375, -8.628379],
                            [122.235470, -8.628221],
                            [122.235457, -8.628134],
                            [122.235309, -8.628155],
                            [122.235349, -8.628398],
                            [122.235299, -8.628357],
                            [122.235197, -8.628233],
                            [122.235288, -8.627912],
                            [122.235275, -8.627788],
                            [122.235293, -8.627619],
                            [122.235235, -8.627518],
                            [122.235192, -8.627420],
                            [122.234999, -8.627730],
                            [122.234871, -8.627785],
                            [122.234830, -8.627834],
                            [122.234721, -8.627924],
                            [122.234587, -8.628229],
                            [122.234602, -8.628375],
                            [122.234518, -8.628596],
                            [122.234458, -8.628645],
                            [122.234524, -8.628700],
                            [122.234460, -8.628869],
                            [122.234417, -8.629013],
                            [122.234340, -8.628920],
                            [122.234374, -8.628600],
                            [122.234361, -8.628474],
                            [122.234465, -8.628330],
                            [122.234426, -8.627936],
                            [122.234512, -8.627788],
                            [122.234553, -8.627580],
                            [122.234436, -8.627517],
                            [122.234375, -8.627788],
                            [122.234238, -8.627976],
                            [122.234113, -8.628080],
                            [122.233961, -8.628145],
                            [122.233875, -8.628194],
                            [122.233751, -8.628235],
                            [122.233694, -8.627782],
                            [122.233353, -8.627741],
                            [122.233239, -8.627876],
                            [122.233151, -8.627917],
                            [122.233103, -8.627646],
                            [122.233033, -8.627587],
                            [122.232463, -8.627649],
                            [122.232422, -8.627528],
                            [122.232606, -8.627238],
                            [122.232441, -8.627190],
                            [122.232261, -8.627208],
                            [122.232088, -8.627190],
                            [122.231978, -8.627058],
                            [122.231809, -8.627014],
                            [122.231642, -8.627109],
                            [122.231548, -8.626995],
                            [122.231568, -8.626798],
                            [122.231486, -8.626655],
                            [122.231374, -8.626606],
                            [122.231333, -8.626557],
                            [122.231229, -8.626515],
                            [122.231246, -8.626689],
                            [122.231191, -8.626784],
                            [122.231243, -8.626967],
                            [122.231001, -8.627010],
                            [122.230815, -8.627232],
                            [122.230564, -8.627339],
                            [122.230402, -8.627533],
                            [122.230327, -8.627595],
                            [122.230340, -8.627727],
                            [122.230306, -8.627755],
                            [122.230235, -8.627642],
                            [122.230344, -8.627391],
                            [122.230423, -8.627328],
                            [122.230464, -8.627188],
                            [122.230651, -8.627148],
                            [122.230781, -8.627072],
                            [122.230828, -8.626962],
                            [122.230980, -8.626707],
                            [122.231106, -8.626606],
                            [122.231147, -8.626443],
                            [122.231035, -8.626253],
                            [122.230662, -8.626172],
                            [122.230600, -8.625887],
                            [122.230492, -8.625856],
                            [122.230513, -8.625832],
                            [122.230602, -8.625754],
                            [122.230650, -8.625666],
                            [122.230299, -8.625608],
                            [122.230243, -8.625796],
                            [122.230384, -8.625921],
                            [122.230312, -8.625985],
                            [122.229977, -8.625965],
                            [122.229763, -8.626021],
                            [122.229254, -8.625990],
                            [122.229020, -8.626073],
                            [122.228952, -8.625924],
                            [122.228423, -8.625831],
                            [122.228063, -8.625511],
                            [122.227938, -8.625454],
                            [122.227588, -8.625474],
                            [122.227472, -8.625603],
                            [122.227371, -8.625690],
                            [122.227285, -8.625594],
                            [122.227303, -8.625312],
                            [122.227000, -8.625093],
                            [122.226743, -8.625013],
                            [122.226655, -8.624965],
                            [122.226516, -8.624922],
                            [122.226346, -8.624830],
                            [122.225835, -8.624785],
                            [122.225702, -8.624692],
                            [122.225346, -8.624625],
                            [122.225247, -8.624586],
                            [122.225475, -8.624423],
                            [122.225654, -8.624285],
                            [122.225762, -8.624236],
                            [122.225836, -8.624145],
                            [122.225655, -8.624061],
                            [122.225546, -8.624002],
                            [122.225635, -8.623839],
                            [122.226210, -8.623786],
                            [122.226316, -8.623793],
                            [122.226537, -8.623780],
                            [122.226610, -8.623699],
                            [122.226665, -8.623702],
                            [122.226772, -8.623821],
                            [122.226842, -8.623880],
                            [122.226837, -8.623790],
                            [122.226911, -8.623702],
                            [122.227027, -8.623955],
                            [122.227299, -8.624018],
                            [122.227425, -8.624158],
                            [122.227643, -8.624146],
                            [122.227745, -8.624201],
                            [122.227929, -8.624244],
                            [122.228110, -8.624293],
                            [122.228274, -8.624205],
                            [122.228337, -8.624341],
                            [122.228441, -8.624335],
                            [122.228606, -8.624153],
                            [122.228702, -8.624067],
                            [122.228723, -8.624044],
                            [122.228769, -8.624044],
                            [122.228769, -8.624134],
                            [122.228749, -8.624160],
                            [122.228697, -8.624199],
                            [122.228567, -8.624366],
                            [122.228681, -8.624554],
                            [122.228881, -8.624709],
                            [122.228947, -8.624550],
                            [122.229167, -8.624583],
                            [122.229086, -8.624406]])


# noinspection PyUnresolvedReferences
def get_qgis_app():
    """ Start one QGIS application to test against.

    :returns: Handle to QGIS app, canvas, iface and parent. If there are any
        errors the tuple members will be returned as None.
    :rtype: (QgsApplication, CANVAS, IFACE, PARENT)

    If QGIS is already running the handle to that app will be returned.
    """

    try:
        from PyQt4 import QtGui, QtCore
        from qgis.core import QgsApplication
        from qgis.gui import QgsMapCanvas
        from safe.common.qgis_interface import QgisInterface
    except ImportError:
        return None, None, None, None

    global QGIS_APP  # pylint: disable=W0603

    if QGIS_APP is None:
        gui_flag = True  # All test will run qgis in gui mode
        #noinspection PyPep8Naming
        QGIS_APP = QgsApplication(sys.argv, gui_flag)
        # Make sure QGIS_PREFIX_PATH is set in your env if needed!
        QGIS_APP.initQgis()
        s = QGIS_APP.showSettings()
        LOGGER.debug(s)

    global PARENT  # pylint: disable=W0603
    if PARENT is None:
        #noinspection PyPep8Naming
        PARENT = QtGui.QWidget()

    global CANVAS  # pylint: disable=W0603
    if CANVAS is None:
        #noinspection PyPep8Naming
        CANVAS = QgsMapCanvas(PARENT)
        CANVAS.resize(QtCore.QSize(400, 400))

    global IFACE  # pylint: disable=W0603
    if IFACE is None:
        # QgisInterface is a stub implementation of the QGIS plugin interface
        #noinspection PyPep8Naming
        IFACE = QgisInterface(CANVAS)

    return QGIS_APP, CANVAS, IFACE, PARENT
