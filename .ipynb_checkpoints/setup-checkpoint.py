from setuptools import setup

setup(name='UniswapPy',
      version='0.1',
      description='Uniswap for Python',
      url='http://github.com/icmoore/uniswappy',
      author = "icmoore",
      author_email = "imoore@syscoin.org",
      license='MIT',
      package_dir = {"uniswappy": "src/prod"},
      packages=[
          'uniswappy.cpt.exchg',
          'uniswappy.cpt.factory',
          'uniswappy.cpt.index',
          'uniswappy.cpt.quote',
          'uniswappy.cpt.wallet',
          'uniswappy.erc',
          'uniswappy.math.basic',
          'uniswappy.math.basic',
          'uniswappy.math.interest',
          'uniswappy.math.interest.ips',
          'uniswappy.math.interest.ips.aggregate',
          'uniswappy.math.model',
          'uniswappy.math.risk',
          'uniswappy.process',
          'uniswappy.process.deposit',
          'uniswappy.process.deposit',
          'uniswappy.process.liquidity',
          'uniswappy.process.swap',
          'uniswappy.simulate',   
          'src.prod.cpt.exchg',
          'src.prod.cpt.factory',
          'src.prod.cpt.index',
          'src.prod.cpt.quote',
          'src.prod.cpt.wallet',
          'src.prod.erc',
          'src.prod.math.basic',
          'src.prod.math.basic',
          'src.prod.math.interest',
          'src.prod.math.interest.ips',
          'src.prod.math.interest.ips.aggregate',
          'src.prod.math.model',
          'src.prod.math.risk',
          'src.prod.process',
          'src.prod.process.deposit',
          'src.prod.process.deposit',
          'src.prod.process.liquidity',
          'src.prod.process.swap',
          'src.prod.simulate',
      ],
      zip_safe=False)
