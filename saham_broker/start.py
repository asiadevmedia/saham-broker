import os
import sys
import time
import telepot
import pyautogui
import pythoncom
import win32com.client as client
from telepot.loop import MessageLoop
from func import *

sys.tracebacklimit=0

here = os.path.abspath(os.path.dirname(__file__))
filename = here + "\\tmp.png";

class Abroker(telepot.Bot):

	def __init__(self, *args, **kwargs):
		super(Abroker, self).__init__(*args, **kwargs);
		self.answerer = telepot.helper.Answerer(self);
		print ('Login bot...');

	def on_chat_message(self, msg):
		content_type, chat_type, chat_id = telepot.glance(msg)

		if chat_id in adminId:
			if content_type == 'text':
				fn = msg['text'][1:4];
				fncode = ['pix', 'acm', 'gup', 'fib'];
				if fn == 'pix':
					tab = "0";
				elif fn == 'acm':
					fn = 'acm';
					tab = "1";
				elif fn == 'gup':
					tab = "2";
				elif fn == 'fib':
					tab = "3";
				
				charts = msg['text'][5:9];
				chartscode = ['aapl', 'aali', 'abba', 'abda', 'abmm', 'aces', 'acst', 'ades', 'adhi', 'admf', 'admg', 'adro', 'agii', 'agro', 'agrs', 'ahap', 'aims', 'aisa', 'akku', 'akpi', 'akra', 'aksi', 'aldo', 'alka', 'almi', 'alto', 'amag', 'amfg', 'amin', 'amrt', 'andi', 'anjt', 'antm', 'apex', 'apic', 'apii', 'apli', 'apln', 'apol', 'argo', 'arii', 'army', 'arna', 'arta', 'arti', 'arto', 'asbi', 'asdm', 'asgr', 'asii', 'asjt', 'asmi', 'asri', 'asrm', 'assa', 'atic', 'atpk', 'auto', 'babp', 'baca', 'baja', 'bali', 'bapa', 'bata', 'bayu', 'bbca', 'bbhi', 'bbkp', 'bbld', 'bbmd', 'bbni', 'bbnp', 'bbri', 'bbrm', 'bbtn', 'bbyb', 'bcap', 'bcic', 'bcip', 'bdmn', 'beks', 'bell', 'best', 'bfin', 'bgtg', 'bhit', 'bika', 'bima', 'bina', 'bipi', 'bipp', 'bird', 'bisi', 'bjbr', 'bjtm', 'bkdp', 'bksl', 'bksw', 'blta', 'bltz', 'bmas', 'bmri', 'bmsr', 'bmtr', 'bnba', 'bnbr', 'bnga', 'bnii', 'bnli', 'boga', 'bolt', 'born', 'boss', 'bpfi', 'bpii', 'bram', 'bris', 'brms', 'brna', 'brpt', 'bsde', 'bsim', 'bssr', 'bswd', 'btek', 'btel', 'bton', 'btpn', 'btpr', 'btps', 'budi', 'bukk', 'bull', 'bumi', 'buva', 'bvic', 'bwpt', 'byan', 'camp', 'cani', 'cars', 'casa', 'cass', 'ceka', 'cent', 'cfin', 'cint', 'cita', 'city', 'ckra', 'cleo', 'clpi', 'cmnp', 'cmpp', 'cnko', 'cntx', 'cowl', 'cpin', 'cpro', 'csap', 'csis', 'ctbn', 'ctra', 'ctth', 'dart', 'daya', 'defi', 'dewa', 'dfam', 'dgik', 'dild', 'digi', 'dkft', 'dlta', 'dmas', 'dnar', 'dnet', 'doid', 'dpns', 'dpum', 'dsfi', 'dsng', 'dssa', 'duck', 'duti', 'dvla', 'dwgl', 'dyan', 'ecii', 'ekad', 'elsa', 'elty', 'emde', 'emtk', 'enrg', 'epmt', 'eraa', 'ertx', 'essa', 'esti', 'etwa', 'excl', 'fast', 'fasw', 'film', 'finn', 'fire', 'fish', 'fmii', 'foru', 'forz', 'fpni', 'fren', 'gama', 'gdst', 'gdyr', 'gema', 'gems', 'ggrm', 'ghon', 'giaa', 'gjtl', 'glob', 'gmcw', 'gmfi', 'gmtd', 'gold', 'goll', 'good', 'gpra', 'gren', 'gsmf', 'gtbo', 'gwsa', 'gzco', 'hade', 'hdfa', 'hdtx', 'heal', 'heli', 'hero', 'hexa', 'hits', 'hkmu', 'hmsp', 'hoki', 'home', 'hotl', 'hrta', 'hrum', 'iata', 'ibfn', 'ibst', 'icbp', 'icon', 'idpr', 'igar', 'iikp', 'ikai', 'ikbi', 'imas', 'imjs', 'impc', 'inaf', 'inai', 'incf', 'inci', 'inco', 'indf', 'indr', 'inds', 'indx', 'indy', 'inkp', 'inpc', 'inpp', 'inps', 'inru', 'inta', 'intd', 'intp', 'ipcc', 'ipcm', 'ipol', 'isat', 'issp', 'itma', 'itmg', 'ittg', 'jawa', 'jecc', 'jgle', 'jihd', 'jkon', 'jksw', 'jmas', 'jpfa', 'jprs', 'jrpt', 'jsky', 'jsmr', 'jspt', 'jtpe', 'kaef', 'karw', 'kbli', 'kblm', 'kblv', 'kbri', 'kdsi', 'kias', 'kici', 'kija', 'kino', 'kios', 'kkgi', 'klbf', 'kmtr', 'kobx', 'koin', 'koni', 'kopi', 'kpal', 'kpas', 'kpig', 'krah', 'kras', 'kren', 'land', 'lapd', 'lcgp', 'lckm', 'lead', 'link', 'lion', 'lmas', 'lmpi', 'lmsh', 'lpck', 'lpgi', 'lpin', 'lpkr', 'lpli', 'lppf', 'lpps', 'lrna', 'lsip', 'ltls', 'maba', 'magp', 'main', 'mami', 'mapa', 'mapb', 'mapi', 'mari', 'mark', 'masa', 'maya', 'mbap', 'mbss', 'mbto', 'mcas', 'mcor', 'mdia', 'mdka', 'mdki', 'mdln', 'mdrn', 'medc', 'mega', 'merk', 'meta', 'mfin', 'mfmi', 'mgna', 'mgro', 'mice', 'midi', 'mika', 'mina', 'mira', 'miti', 'mknt', 'mkpi', 'mlbi', 'mlia', 'mlpl', 'mlpt', 'mmlp', 'mncn', 'moli', 'mpmx', 'mpow', 'mppa', 'mpro', 'mrat', 'mrei', 'msin', 'msky', 'mtdl', 'mtfn', 'mtla', 'mtra', 'mtsm', 'mtwi', 'myoh', 'myor', 'myrx', 'mytx', 'naga', 'nasa', 'nely', 'nfcx', 'nick', 'nikl', 'nips', 'niro', 'nisp', 'nobu', 'nrca', 'nusa', 'oasa', 'ocap', 'okas', 'omre', 'padi', 'palm', 'pani', 'panr', 'pans', 'pbid', 'pbrx', 'pbsa', 'pcar', 'pdes', 'pege', 'pgas', 'pgli', 'pico', 'pjaa', 'pkpk', 'plas', 'plin', 'pnbn', 'pnbs', 'pnin', 'pnlf', 'pnse', 'poll', 'poly', 'pool', 'port', 'powr', 'ppre', 'ppro', 'pras', 'prda', 'prim', 'psab', 'psdn', 'pskt', 'pssi', 'ptba', 'ptis', 'ptpp', 'ptro', 'ptsn', 'ptsp', 'pudp', 'pwon', 'pyfa', 'pzza', 'raja', 'rals', 'ranc', 'rbms', 'rdtx', 'reli', 'ricy', 'rigs', 'rimo', 'rise', 'rmba', 'roda', 'roti', 'ruis', 'safe', 'same', 'sapx', 'scbd', 'scco', 'scma', 'scpi', 'sdmu', 'sdpc', 'sdra', 'sgro', 'shid', 'ship', 'siap', 'sido', 'silo', 'sima', 'simp', 'sipd', 'skbm', 'sklt', 'skrn', 'skyb', 'smar', 'smbr', 'smcb', 'smdm', 'smdr', 'smgr', 'smma', 'smmt', 'smra', 'smru', 'smsm', 'soci', 'sona', 'spma', 'spto', 'sqmi', 'sraj', 'sril', 'srsn', 'srtg', 'ssia', 'ssms', 'sstm', 'star', 'sttp', 'sugi', 'suli', 'supr', 'sure', 'swat', 'talf', 'tamu', 'tara', 'taxi', 'tbig', 'tbla', 'tbms', 'tcid', 'tcpi', 'tdpm', 'tele', 'tfco', 'tgka', 'tgra', 'tifa', 'tins', 'tira', 'tirt', 'tkim', 'tlkm', 'tmas', 'tmpi', 'tmpo', 'tnca', 'toba', 'tops', 'totl', 'toto', 'towr', 'tpia', 'tpma', 'tram', 'tril', 'trim', 'trio', 'tris', 'trst', 'truk', 'trus', 'tspc', 'tugu', 'turi', 'ultj', 'unic', 'unit', 'unsp', 'untr', 'unvr', 'vico', 'vins', 'viva', 'voks', 'vrna', 'wapo', 'wege', 'weha', 'wico', 'wiim', 'wika', 'wins', 'womf', 'wood', 'wsbp', 'wskt', 'wton', 'ypas', 'yule', 'zbra', 'zinc']; 
				time = msg['text'][9:];

				if msg['text'] == '/help':
					text = "Welcome \n Bantuan - /help\n Pixel - /pix -> kode saham -> interval\n Gupy - /gup -> kode saham -> interval";
					bot.sendMessage(chat_id, text, parse_mode='Markdown');

				if msg['text'] == '/'+fn:
					if fn in fncode:
						bot.sendChatAction(chat_id, 'typing');
						self.dayli(tab);
						bot.sendPhoto(chat_id, photo=open(filename, 'rb'), caption=('[' + fn.upper() + '] ' + 'TimeFrame:' + 'Dayli'));
						os.remove(filename);
					else:
						bot.sendMessage(chat_id, "Maaf..Kode command tidak dapat kami temukan.", parse_mode='Markdown');

				if msg['text'] == '/'+ fn + ' '+ charts:
					if charts in chartscode:
						bot.sendChatAction(chat_id, 'typing');
						time = '86400';
						self.chart(charts, tab, time);
						bot.sendPhoto(chat_id, photo=open(filename, 'rb'), caption=('[' + fn.upper() + '] ' + charts.upper() + ' - ' + 'TimeFrame:' + 'Dayli'));
						os.remove(filename);
					else:
						bot.sendMessage(chat_id, "Maaf..Kode saham tidak dapat kami temukan.", parse_mode='Markdown');

				elif msg['text'] == '/'+ fn + ' '+ charts + time:
					if charts in chartscode:
						bot.sendChatAction(chat_id, 'typing');
						self.charttime(charts, tab, time);
						bot.sendPhoto(chat_id, photo=open(filename, 'rb'), caption=('[' + fn.upper() + '] ' + charts.upper() + ' - ' + 'TimeFrame:' + time + '-minute'));
						os.remove(filename);
					else:
						bot.sendMessage(chat_id, "Maaf..Kode saham tidak dapat kami temukan.", parse_mode='Markdown');
		else:
			bot.sendMessage(chat_id, "Tidak di ijinkan di group ini");

	def dayli(self, tab):
		pythoncom.CoInitialize();
		AB = client.Dispatch("Broker.Application");
		ABDocs = AB.Documents;
		AD = ABDocs.Item(0);
		AD.Interval = 86400;
		AW = AB.ActiveWindow;
		AW.SelectedTab = tab;
		AW.ExportImage( filename, 720, 480);
		return

	def chart(self, charts, tab, time):
		times = int(time);
		pythoncom.CoInitialize();
		AB = client.Dispatch("Broker.Application");
		AW = AB.ActiveWindow;
		ABDocs = AB.Documents;
		AD = ABDocs.Item(0);
		AD.Name = charts;
		AD.Interval = times;
		AW.SelectedTab = tab;
		AW.ExportImage( filename, 720, 480);
		return

	def charttime(self, charts, tab, time):
		x = int(60);
		y = int(time);
		inter = x*y;
		pythoncom.CoInitialize();
		AB = client.Dispatch("Broker.Application");
		AW = AB.ActiveWindow;
		ABDocs = AB.Documents;
		AD = ABDocs.Item(0);
		AD.Name = charts;
		AD.Interval = inter;
		AW.SelectedTab = tab;
		AW.ExportImage( filename, 720, 480);
		return

TOKEN = telegrambot;
bot = Abroker(TOKEN);
MessageLoop(bot).run_as_thread();
print('Bot siap digunakan');
while 1:
	time.sleep(10)