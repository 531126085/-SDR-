#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: Top Block
# Generated: Thu Mar  7 10:21:36 2019
##################################################

if __name__ == '__main__':
    import ctypes
    import sys
    if sys.platform.startswith('linux'):
        try:
            x11 = ctypes.cdll.LoadLibrary('libX11.so')
            x11.XInitThreads()
        except:
            print "Warning: failed to XInitThreads()"

from PyQt4 import Qt
from gnuradio import blocks
from gnuradio import digital
from gnuradio import eng_notation
from gnuradio import gr
from gnuradio import qtgui
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from gnuradio.qtgui import Range, RangeWidget
from grc_gnuradio import blks2 as grc_blks2
from optparse import OptionParser
import osmosdr
import sip
import sys
import time
from gnuradio import qtgui


class top_block(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "Top Block")
        Qt.QWidget.__init__(self)
        self.setWindowTitle("Top Block")
        qtgui.util.check_set_qss()
        try:
            self.setWindowIcon(Qt.QIcon.fromTheme('gnuradio-grc'))
        except:
            pass
        self.top_scroll_layout = Qt.QVBoxLayout()
        self.setLayout(self.top_scroll_layout)
        self.top_scroll = Qt.QScrollArea()
        self.top_scroll.setFrameStyle(Qt.QFrame.NoFrame)
        self.top_scroll_layout.addWidget(self.top_scroll)
        self.top_scroll.setWidgetResizable(True)
        self.top_widget = Qt.QWidget()
        self.top_scroll.setWidget(self.top_widget)
        self.top_layout = Qt.QVBoxLayout(self.top_widget)
        self.top_grid_layout = Qt.QGridLayout()
        self.top_layout.addLayout(self.top_grid_layout)

        self.settings = Qt.QSettings("GNU Radio", "top_block")
        self.restoreGeometry(self.settings.value("geometry").toByteArray())

        ##################################################
        # Variables
        ##################################################
        self.tx_RF_Gain = tx_RF_Gain = 18
        self.samp_rate = samp_rate = 500000
        self.rx_RF_Gain = rx_RF_Gain = 18

        ##################################################
        # Blocks
        ##################################################
        self._tx_RF_Gain_range = Range(0, 50, 1, 18, 200)
        self._tx_RF_Gain_win = RangeWidget(self._tx_RF_Gain_range, self.set_tx_RF_Gain, 'tx_RF_Gain', "counter_slider", int)
        self.top_layout.addWidget(self._tx_RF_Gain_win)
        self._rx_RF_Gain_range = Range(0, 50, 1, 18, 200)
        self._rx_RF_Gain_win = RangeWidget(self._rx_RF_Gain_range, self.set_rx_RF_Gain, "rx_RF_Gain", "counter_slider", int)
        self.top_layout.addWidget(self._rx_RF_Gain_win)
        self.qtgui_sink_x_1 = qtgui.sink_c(
        	4096, #fftsize
        	firdes.WIN_BLACKMAN_hARRIS, #wintype
        	915000000, #fc
        	500000, #bw
        	"send_fft", #name
        	True, #plotfreq
        	True, #plotwaterfall
        	True, #plottime
        	True, #plotconst
        )
        self.qtgui_sink_x_1.set_update_time(1.0/10)
        self._qtgui_sink_x_1_win = sip.wrapinstance(self.qtgui_sink_x_1.pyqwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._qtgui_sink_x_1_win)

        self.qtgui_sink_x_1.enable_rf_freq(False)



        self.qtgui_sink_x_0 = qtgui.sink_c(
        	4096, #fftsize
        	firdes.WIN_BLACKMAN_hARRIS, #wintype
        	915000000, #fc
        	500000, #bw
        	"", #name
        	True, #plotfreq
        	True, #plotwaterfall
        	True, #plottime
        	True, #plotconst
        )
        self.qtgui_sink_x_0.set_update_time(1.0/10)
        self._qtgui_sink_x_0_win = sip.wrapinstance(self.qtgui_sink_x_0.pyqwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._qtgui_sink_x_0_win)

        self.qtgui_sink_x_0.enable_rf_freq(False)



        self.osmosdr_source_0 = osmosdr.source( args="numchan=" + str(1) + " " + 'driver=lime,soapy=0' )
        self.osmosdr_source_0.set_sample_rate(samp_rate)
        self.osmosdr_source_0.set_center_freq(915e6, 0)
        self.osmosdr_source_0.set_freq_corr(0, 0)
        self.osmosdr_source_0.set_dc_offset_mode(2, 0)
        self.osmosdr_source_0.set_iq_balance_mode(0, 0)
        self.osmosdr_source_0.set_gain_mode(False, 0)
        self.osmosdr_source_0.set_gain(rx_RF_Gain, 0)
        self.osmosdr_source_0.set_if_gain(0, 0)
        self.osmosdr_source_0.set_bb_gain(0, 0)
        self.osmosdr_source_0.set_antenna('LNAW', 0)
        self.osmosdr_source_0.set_bandwidth(500000, 0)

        self.osmosdr_sink_0 = osmosdr.sink( args="numchan=" + str(1) + " " + 'driver=lime,soapy=0' )
        self.osmosdr_sink_0.set_sample_rate(samp_rate)
        self.osmosdr_sink_0.set_center_freq(915e6, 0)
        self.osmosdr_sink_0.set_freq_corr(0, 0)
        self.osmosdr_sink_0.set_gain(tx_RF_Gain, 0)
        self.osmosdr_sink_0.set_if_gain(0, 0)
        self.osmosdr_sink_0.set_bb_gain(0, 0)
        self.osmosdr_sink_0.set_antenna('BAND1', 0)
        self.osmosdr_sink_0.set_bandwidth(500000, 0)

        self.digital_gmsk_mod_0 = digital.gmsk_mod(
        	samples_per_symbol=8,
        	bt=0.35,
        	verbose=False,
        	log=False,
        )
        self.digital_gmsk_demod_0 = digital.gmsk_demod(
        	samples_per_symbol=8,
        	gain_mu=0.175,
        	mu=0.5,
        	omega_relative_limit=0.005,
        	freq_error=0.0,
        	verbose=False,
        	log=False,
        )
        self.blocks_file_source_0 = blocks.file_source(gr.sizeof_gr_complex*1, '/home/wang/LimeSDR_RW_test/send.txt', True)
        self.blocks_file_sink_0 = blocks.file_sink(gr.sizeof_gr_complex*1, '/home/wang/LimeSDR_RW_test/receive.txt', False)
        self.blocks_file_sink_0.set_unbuffered(False)
        self.blks2_packet_encoder_0 = grc_blks2.packet_mod_c(grc_blks2.packet_encoder(
        		samples_per_symbol=2,
        		bits_per_symbol=1,
        		preamble='',
        		access_code='',
        		pad_for_usrp=True,
        	),
        	payload_length=0,
        )
        self.blks2_packet_decoder_0 = grc_blks2.packet_demod_c(grc_blks2.packet_decoder(
        		access_code='',
        		threshold=-1,
        		callback=lambda ok, payload: self.blks2_packet_decoder_0.recv_pkt(ok, payload),
        	),
        )

        ##################################################
        # Connections
        ##################################################
        self.connect((self.blks2_packet_decoder_0, 0), (self.blocks_file_sink_0, 0))
        self.connect((self.blks2_packet_encoder_0, 0), (self.digital_gmsk_mod_0, 0))
        self.connect((self.blocks_file_source_0, 0), (self.blks2_packet_encoder_0, 0))
        self.connect((self.digital_gmsk_demod_0, 0), (self.blks2_packet_decoder_0, 0))
        self.connect((self.digital_gmsk_mod_0, 0), (self.osmosdr_sink_0, 0))
        self.connect((self.digital_gmsk_mod_0, 0), (self.qtgui_sink_x_1, 0))
        self.connect((self.osmosdr_source_0, 0), (self.digital_gmsk_demod_0, 0))
        self.connect((self.osmosdr_source_0, 0), (self.qtgui_sink_x_0, 0))

    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "top_block")
        self.settings.setValue("geometry", self.saveGeometry())
        event.accept()

    def get_tx_RF_Gain(self):
        return self.tx_RF_Gain

    def set_tx_RF_Gain(self, tx_RF_Gain):
        self.tx_RF_Gain = tx_RF_Gain
        self.osmosdr_sink_0.set_gain(self.tx_RF_Gain, 0)

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.osmosdr_source_0.set_sample_rate(self.samp_rate)
        self.osmosdr_sink_0.set_sample_rate(self.samp_rate)

    def get_rx_RF_Gain(self):
        return self.rx_RF_Gain

    def set_rx_RF_Gain(self, rx_RF_Gain):
        self.rx_RF_Gain = rx_RF_Gain
        self.osmosdr_source_0.set_gain(self.rx_RF_Gain, 0)


def main(top_block_cls=top_block, options=None):

    from distutils.version import StrictVersion
    if StrictVersion(Qt.qVersion()) >= StrictVersion("4.5.0"):
        style = gr.prefs().get_string('qtgui', 'style', 'raster')
        Qt.QApplication.setGraphicsSystem(style)
    qapp = Qt.QApplication(sys.argv)

    tb = top_block_cls()
    tb.start()
    tb.show()

    def quitting():
        tb.stop()
        tb.wait()
    qapp.connect(qapp, Qt.SIGNAL("aboutToQuit()"), quitting)
    qapp.exec_()


if __name__ == '__main__':
    main()
