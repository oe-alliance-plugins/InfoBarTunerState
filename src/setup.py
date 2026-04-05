from setuptools import setup
import setup_translate

pkg = 'Extensions.InfoBarTunerState'
setup(name='enigma2-plugin-extensions-infobartunerstate',
       version='3.0',
       description='Show the tuner state as infobar popup',
       package_dir={pkg: 'InfoBarTunerState'},
       packages=[pkg],
       package_data={pkg: ['images/*.png', '*.png', '*.xml', 'locale/*/LC_MESSAGES/*.mo', 'skin_HD.xml', 'skin_FHD.xml', 'stopped.png', 'stream.png', 'background.png', 'finished.png', 'info.png', 'progress.png', 'record.png', 'plugin.png', 'maintainer.info', 'LICENSE']},
       cmdclass=setup_translate.cmdclass,  # for translation
      )
