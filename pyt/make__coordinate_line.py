import numpy as np

# ========================================================= #
# ===  make__coordinate                                 === #
# ========================================================= #

def make__coordinate_line():

    x_,y_,z_ = 0, 1, 2

    # ------------------------------------------------- #
    # --- [1] parameter                             --- #
    # ------------------------------------------------- #
    pt1         = [ 0.0, 0.0, +0.00 ]
    pt2         = [ 0.0, 0.0, -0.20 ]
    nDiv        = 101

    sdist       = np.linspace( 0.0, 1.0, nDiv )
    coord       = np.zeros( (nDiv,3) )
    coord[:,x_] = pt1[x_] + ( pt2[x_] - pt1[x_] ) * sdist
    coord[:,y_] = pt1[y_] + ( pt2[y_] - pt1[y_] ) * sdist
    coord[:,z_] = pt1[z_] + ( pt2[z_] - pt1[z_] ) * sdist

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
    make__coordinate_line()


    
