import numpy as np

# ========================================================= #
# ===  make__coordinate_grid                            === #
# ========================================================= #

def make__coordinate_grid():

    x_,y_,z_ = 0, 1, 2

    # ------------------------------------------------- #
    # --- [1] parameter                             --- #
    # ------------------------------------------------- #
    import nkUtilities.equiSpaceGrid as esg
    x1MinMaxNum = [ 0.0, 1.0, 11 ]
    x2MinMaxNum = [ 0.0, 1.0, 11 ]
    x3MinMaxNum = [ 0.0, 1.0, 11 ]
    coord       = esg.equiSpaceGrid( x1MinMaxNum=x1MinMaxNum, x2MinMaxNum=x2MinMaxNum, \
                                     x3MinMaxNum=x3MinMaxNum, returnType = "point" )
    
    # ------------------------------------------------- #
    # --- [2] save in file                          --- #
    # ------------------------------------------------- #
    outFile   = "dat/out.dat"
    import nkUtilities.save__pointFile as spf
    spf.save__pointFile( outFile=outFile, Data=coord )


# ========================================================= #
# ===   実行部                                          === #
# ========================================================= #

if ( __name__=="__main__" ):
    make__coordinate_grid()

