# -*- python -*-
# automatically generated wscript

import waflib.Logs as msg

PACKAGE = {
    'name': 'boost-tests',
    'author': ["Sebastien Binet"], 
}

def pkg_deps(ctx):
    ctx.use_pkg('pkg-settings')
    return

def options(ctx):
    ctx.load('find_boost')
    
def configure(ctx):
    ctx.load('find_boost')
    ctx.find_boost(lib='filesystem system')
    ctx.start_msg("was Boost found ?")
    ctx.end_msg(ctx.env.HWAF_FOUND_BOOST)
    if ctx.env.HWAF_FOUND_BOOST:
        ctx.start_msg("boost version")
        ctx.end_msg(ctx.env.BOOST_VERSION)
    else:
        msg.fatal("Boost could not be found")

def build(ctx):
    ctx.build_app(
        name     = "test-hwaf-boost-filesystem",
        source   = "src/main-boost-filesystem.cxx",
        use      = ["boost-filesystem", "boost-system"],
        )
    return
