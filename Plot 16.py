
import chart_studio.plotly as py
from plotly.graph_objs import *

trace1 = {
  "line": {"shape": "spline"}, 
  "meta": {"columnNames": {
      "x": "D", 
      "y": "A"
    }}, 
  "mode": "markers+lines", 
  "name": "10 ms", 
  "type": "scatter", 
  "x": ["25", "50", "75", "100", "125", "150", "175", "200", "225", "250", "275", "300", "325", "350", "375", "400", "425", "450", "475", "500"], 
  "y": ["0.1586119374593663", "0.1379812507242666", "0.12522090916176637", "0.11273087876573226", "0.098562714338169", "0.09975877661670841", "0.09560917400538839", "0.09218961991862332", "0.0900225854269015", "0.08988509982271066", "0.0915514164393864", "0.09148805614787642", "0.0916136023949443", "0.08910321725504076", "0.09078983891589472", "0.0929092707630198", "0.08924034685718414", "0.09076784508842721", "0.08880943377722354", "0.08830158713921701"], 
  "stackgroup": None
}
trace2 = {
  "line": {"shape": "spline"}, 
  "meta": {"columnNames": {
      "x": "D", 
      "y": "A"
    }}, 
  "mode": "markers+lines", 
  "name": "50 ms", 
  "type": "scatter", 
  "x": ["25", "50", "75", "100", "125", "150", "175", "200", "225", "250", "275", "300", "325", "350", "375", "400", "425", "450", "475", "500"], 
  "y": ["0.41476137347787045", "0.356072803782796", "0.32729619286022993", "0.3115861843574562", "0.25772287175076053", "0.25869587755003653", "0.2674256563891691", "0.2561922896030668", "0.24925626633909978", "0.2507219416493954", "0.2512714376678703", "0.24124374063375612", "0.23850808494086043", "0.25073887148234", "0.2399277967584913", "0.2441102460787512", "0.24501411004711143", "0.24076761201739166", "0.2488017862251562", "0.2414877488361023"], 
  "stackgroup": None
}
trace3 = {
  "line": {"shape": "spline"}, 
  "meta": {"columnNames": {
      "x": "D", 
      "y": "A"
    }}, 
  "mode": "markers+lines", 
  "name": "100 ms", 
  "type": "scatter", 
  "x": ["25", "50", "75", "100", "125", "150", "175", "200", "225", "250", "275", "300", "325", "350", "375", "400", "425", "450", "475", "500"], 
  "y": ["0.47615981088304515", "0.4620053508041334", "0.42534708288955825", "0.38575281990596827", "0.3598803292958557", "0.3562290535438207", "0.34609231534929924", "0.34601724974238474", "0.33285137782321983", "0.33322364393318593", "0.3323187524660941", "0.3397488951352304", "0.3298416532222557", "0.3290553650525908", "0.33644335061044317", "0.3342264146021805", "0.32865677997264725", "0.3365987758285824", "0.3418255423730043", "0.3312280239077974"], 
  "stackgroup": None
}
trace4 = {
  "line": {"shape": "spline"}, 
  "meta": {"columnNames": {
      "x": "D", 
      "y": "A"
    }}, 
  "mode": "markers+lines", 
  "name": "200 ms", 
  "type": "scatter", 
  "x": ["25", "50", "75", "100", "125", "150", "175", "200", "225", "250", "275", "300", "325", "350", "375", "400", "425", "450", "475", "500"], 
  "y": ["0.6441042398022462", "0.6044677108513808", "0.5811805757122397", "0.5460351468765089", "0.5220177314984956", "0.5123741342971181", "0.5056584131219887", "0.5072098893078438", "0.5017664729587729", "0.48329887126123416", "0.4956143755325328", "0.4928694722430253", "0.4817407166295943", "0.49291687391446176", "0.4933923714258826", "0.48319414199818594", "0.4837547955845008", "0.48186791015628083", "0.5001149605471399", "0.4815304370241662"], 
  "stackgroup": None
}
trace5 = {
  "line": {"shape": "spline"}, 
  "meta": {"columnNames": {
      "x": "D", 
      "y": "A"
    }}, 
  "mode": "markers+lines", 
  "name": "500 ms", 
  "type": "scatter", 
  "x": ["25", "50", "75", "100", "125", "150", "175", "200", "225", "250", "275", "300", "325", "350", "375", "400", "425", "450", "475", "500"], 
  "y": ["0.860762849333905", "0.8521078648669347", "0.8239077342620347", "0.79735492135938", "0.7816293976240491", "0.7846942492872808", "0.7769499621070396", "0.7753554991377714", "0.7572281304660262", "0.7621459394303214", "0.7503643687108217", "0.7603157579645574", "0.7468170997817685", "0.7542261538252422", "0.760047747207932", "0.7562875126730026", "0.759544449137578", "0.7555740454092509", "0.75378430547057", "0.7544576181099028"], 
  "stackgroup": None
}
data = [trace1, trace2, trace3, trace4, trace5]
layout = {
  "xaxis": {
    "type": "linear", 
    "range": [-1.2517325017324197, 507.3241510741512], 
    "title": {"text": "Tx-RX distance"}, 
    "autorange": False
  }, 
  "yaxis": {
    "type": "linear", 
    "range": [-0.013392116261413456, 1.0138170089974805], 
    "title": {"text": "VAP"}, 
    "autorange": False
  }, 
  "legend": {
    "x": 0.8041203521864363, 
    "y": 0.9805485970104055, 
    "orientation": "v"
  }, 
  "autosize": True, 
  "template": {
    "data": {
      "bar": [
        {
          "type": "bar", 
          "marker": {"colorbar": {
              "ticks": "", 
              "outlinewidth": 0
            }}
        }
      ], 
      "table": [
        {
          "type": "table", 
          "cells": {
            "fill": {"color": "#EBF0F8"}, 
            "line": {"color": "white"}
          }, 
          "header": {
            "fill": {"color": "#C8D4E3"}, 
            "line": {"color": "white"}
          }
        }
      ], 
      "carpet": [
        {
          "type": "carpet", 
          "aaxis": {
            "gridcolor": "#C8D4E3", 
            "linecolor": "#C8D4E3", 
            "endlinecolor": "#2a3f5f", 
            "minorgridcolor": "#C8D4E3", 
            "startlinecolor": "#2a3f5f"
          }, 
          "baxis": {
            "gridcolor": "#C8D4E3", 
            "linecolor": "#C8D4E3", 
            "endlinecolor": "#2a3f5f", 
            "minorgridcolor": "#C8D4E3", 
            "startlinecolor": "#2a3f5f"
          }
        }
      ], 
      "mesh3d": [
        {
          "type": "mesh3d", 
          "colorbar": {
            "ticks": "", 
            "outlinewidth": 0
          }
        }
      ], 
      "contour": [
        {
          "type": "contour", 
          "colorbar": {
            "ticks": "", 
            "outlinewidth": 0
          }, 
          "autocolorscale": True
        }
      ], 
      "heatmap": [
        {
          "type": "heatmap", 
          "colorbar": {
            "ticks": "", 
            "outlinewidth": 0
          }, 
          "autocolorscale": True
        }
      ], 
      "scatter": [
        {
          "type": "scatter", 
          "marker": {"colorbar": {
              "ticks": "", 
              "outlinewidth": 0
            }}
        }
      ], 
      "surface": [
        {
          "type": "surface", 
          "colorbar": {
            "ticks": "", 
            "outlinewidth": 0
          }
        }
      ], 
      "heatmapgl": [
        {
          "type": "heatmapgl", 
          "colorbar": {
            "ticks": "", 
            "outlinewidth": 0
          }
        }
      ], 
      "histogram": [
        {
          "type": "histogram", 
          "marker": {"colorbar": {
              "ticks": "", 
              "outlinewidth": 0
            }}
        }
      ], 
      "parcoords": [
        {
          "line": {"colorbar": {
              "ticks": "", 
              "outlinewidth": 0
            }}, 
          "type": "parcoords"
        }
      ], 
      "scatter3d": [
        {
          "type": "scatter3d", 
          "marker": {"colorbar": {
              "ticks": "", 
              "outlinewidth": 0
            }}
        }
      ], 
      "scattergl": [
        {
          "type": "scattergl", 
          "marker": {"colorbar": {
              "ticks": "", 
              "outlinewidth": 0
            }}
        }
      ], 
      "choropleth": [
        {
          "type": "choropleth", 
          "colorbar": {
            "ticks": "", 
            "outlinewidth": 0
          }
        }
      ], 
      "scattergeo": [
        {
          "type": "scattergeo", 
          "marker": {"colorbar": {
              "ticks": "", 
              "outlinewidth": 0
            }}
        }
      ], 
      "histogram2d": [
        {
          "type": "histogram2d", 
          "colorbar": {
            "ticks": "", 
            "outlinewidth": 0
          }, 
          "autocolorscale": True
        }
      ], 
      "scatterpolar": [
        {
          "type": "scatterpolar", 
          "marker": {"colorbar": {
              "ticks": "", 
              "outlinewidth": 0
            }}
        }
      ], 
      "contourcarpet": [
        {
          "type": "contourcarpet", 
          "colorbar": {
            "ticks": "", 
            "outlinewidth": 0
          }
        }
      ], 
      "scattercarpet": [
        {
          "type": "scattercarpet", 
          "marker": {"colorbar": {
              "ticks": "", 
              "outlinewidth": 0
            }}
        }
      ], 
      "scattermapbox": [
        {
          "type": "scattermapbox", 
          "marker": {"colorbar": {
              "ticks": "", 
              "outlinewidth": 0
            }}
        }
      ], 
      "scatterpolargl": [
        {
          "type": "scatterpolargl", 
          "marker": {"colorbar": {
              "ticks": "", 
              "outlinewidth": 0
            }}
        }
      ], 
      "scatterternary": [
        {
          "type": "scatterternary", 
          "marker": {"colorbar": {
              "ticks": "", 
              "outlinewidth": 0
            }}
        }
      ], 
      "histogram2dcontour": [
        {
          "type": "histogram2dcontour", 
          "colorbar": {
            "ticks": "", 
            "outlinewidth": 0
          }, 
          "autocolorscale": True
        }
      ]
    }, 
    "layout": {
      "geo": {
        "bgcolor": "white", 
        "showland": True, 
        "lakecolor": "white", 
        "landcolor": "white", 
        "showlakes": True, 
        "subunitcolor": "#C8D4E3"
      }, 
      "font": {"color": "#2a3f5f", "size":18}, 
      "polar": {
        "bgcolor": "white", 
        "radialaxis": {
          "ticks": "", 
          "gridcolor": "#EBF0F8", 
          "linecolor": "#EBF0F8"
        }, 
        "angularaxis": {
          "ticks": "", 
          "gridcolor": "#EBF0F8", 
          "linecolor": "#EBF0F8"
        }
      }, 
      "scene": {
        "xaxis": {
          "ticks": "", 
          "gridcolor": "#DFE8F3", 
          "gridwidth": 2, 
          "linecolor": "#EBF0F8", 
          "zerolinecolor": "#EBF0F8", 
          "showbackground": True, 
          "backgroundcolor": "white"
        }, 
        "yaxis": {
          "ticks": "", 
          "gridcolor": "#DFE8F3", 
          "gridwidth": 2, 
          "linecolor": "#EBF0F8", 
          "zerolinecolor": "#EBF0F8", 
          "showbackground": True, 
          "backgroundcolor": "white"
        }, 
        "zaxis": {
          "ticks": "", 
          "gridcolor": "#DFE8F3", 
          "gridwidth": 2, 
          "linecolor": "#EBF0F8", 
          "zerolinecolor": "#EBF0F8", 
          "showbackground": True, 
          "backgroundcolor": "white"
        }
      }, 
      "title": {"x": 0.05}, 
      "xaxis": {
        "ticks": "", 
        "gridcolor": "#EBF0F8", 
        "linecolor": "#EBF0F8", 
        "automargin": True, 
        "zerolinecolor": "#EBF0F8", 
        "zerolinewidth": 2
      }, 
      "yaxis": {
        "ticks": "", 
        "gridcolor": "#EBF0F8", 
        "linecolor": "#EBF0F8", 
        "automargin": True, 
        "zerolinecolor": "#EBF0F8", 
        "zerolinewidth": 2
      }, 
      "ternary": {
        "aaxis": {
          "ticks": "", 
          "gridcolor": "#DFE8F3", 
          "linecolor": "#A2B1C6"
        }, 
        "baxis": {
          "ticks": "", 
          "gridcolor": "#DFE8F3", 
          "linecolor": "#A2B1C6"
        }, 
        "caxis": {
          "ticks": "", 
          "gridcolor": "#DFE8F3", 
          "linecolor": "#A2B1C6"
        }, 
        "bgcolor": "white"
      }, 
      "colorway": ["#636efa", "#EF553B", "#00cc96", "#ab63fa", "#19d3f3", "#e763fa", "#fecb52", "#ffa15a", "#ff6692", "#b6e880"], 
      "hovermode": "closest", 
      "colorscale": {
        "diverging": [
          [0, "#8e0152"], [0.1, "#c51b7d"], [0.2, "#de77ae"], [0.3, "#f1b6da"], [0.4, "#fde0ef"], [0.5, "#f7f7f7"], [0.6, "#e6f5d0"], [0.7, "#b8e186"], [0.8, "#7fbc41"], [0.9, "#4d9221"], [1, "#276419"]], 
        "sequential": [
          [0, "#0508b8"], [0.0893854748603352, "#1910d8"], [0.1787709497206704, "#3c19f0"], [0.2681564245810056, "#6b1cfb"], [0.3575418994413408, "#981cfd"], [0.44692737430167595, "#bf1cfd"], [0.5363128491620112, "#dd2bfd"], [0.6256983240223464, "#f246fe"], [0.7150837988826816, "#fc67fd"], [0.8044692737430168, "#fe88fc"], [0.8938547486033519, "#fea5fd"], [0.9832402234636871, "#febefe"], [1, "#fec3fe"]], 
        "sequentialminus": [
          [0, "#0508b8"], [0.0893854748603352, "#1910d8"], [0.1787709497206704, "#3c19f0"], [0.2681564245810056, "#6b1cfb"], [0.3575418994413408, "#981cfd"], [0.44692737430167595, "#bf1cfd"], [0.5363128491620112, "#dd2bfd"], [0.6256983240223464, "#f246fe"], [0.7150837988826816, "#fc67fd"], [0.8044692737430168, "#fe88fc"], [0.8938547486033519, "#fea5fd"], [0.9832402234636871, "#febefe"], [1, "#fec3fe"]]
      }, 
      "plot_bgcolor": "white", 
      "paper_bgcolor": "white", 
      "shapedefaults": {
        "line": {"width": 0}, 
        "opacity": 0.4, 
        "fillcolor": "#506784"
      }, 
      "annotationdefaults": {
        "arrowhead": 0, 
        "arrowcolor": "#506784", 
        "arrowwidth": 1
      }
    }, 
    #"themeRef": "PLOTLY_WHITE"
  }
}

fig = Figure(data=data, layout=layout)
fig.write_image("images/AW_50Hz_2.pdf", format='pdf')

#################### 20Hz curve
trace1 = {
  "line": {"shape": "spline"}, 
  "meta": {"columnNames": {
      "x": "D", 
      "y": "A"
    }}, 
  "mode": "markers+lines", 
  "name": "10 ms", 
  "type": "scatter", 
  "x": ["500", "475", "450", "425", "400", "375", "350", "325", "300", "275", "250", "225", "200", "175", "150", "125", "100", "75", "50", "25"], 
  "y": ["0.06984247813628579", "0.06976423233178071", "0.0725029733458406", "0.07361987833580062", "0.07094771773658258", "0.07081193406565091", "0.06961692580897495", "0.06967698270614853", "0.07093950849029329", "0.07071396409003415", "0.07071980548180348", "0.07325996889382282", "0.07293590795507664", "0.06961108616787123", "0.0747079683319452", "0.07270663250631393", "0.07853049139865723", "0.08877569905612662", "0.09692519545196018", "0.10611692944263011"], 
  "visible": True, 
  "stackgroup": None
}
trace2 = {
  "line": {"shape": "spline"}, 
  "meta": {"columnNames": {
      "x": "D", 
      "y": "A"
    }}, 
  "mode": "markers+lines", 
  "name": "50 ms", 
  "type": "scatter", 
  "x": ["25", "50", "75", "100", "125", "150", "175", "200", "225", "250", "275", "300", "325", "350", "375", "400", "425", "450", "475", "500"], 
  "y": ["0.5413878315352161", "0.519753509582169", "0.4645534978119052", "0.4207615851648056", "0.4014448241386161", "0.389547395303397", "0.4100353710280231", "0.40114268266311925", "0.39163229812009653", "0.3932105754423189", "0.38635579487070687", "0.38645305916906963", "0.37147101710283986", "0.38256186416015375", "0.38652015318007593", "0.3738487848844261", "0.3834263867455153", "0.3817476700898253", "0.3780579949218772", "0.3850426358319834"], 
  "visible": True, 
  "stackgroup": None
}
trace3 = {
  "line": {"shape": "spline"}, 
  "meta": {"columnNames": {
      "x": "D", 
      "y": "A"
    }}, 
  "mode": "markers+lines", 
  "name": "100 ms", 
  "type": "scatter", 
  "x": ["25", "50", "75", "100", "125", "150", "175", "200", "225", "250", "275", "300", "325", "350", "375", "400", "425", "450", "475", "500"], 
  "y": ["0.6019404828103967", "0.5548542266686814", "0.52841743983919", "0.47120671342591713", "0.4504967574475364", "0.4288312321566877", "0.4280182978185651", "0.4314422663181082", "0.44583748198255263", "0.4242657038523708", "0.4071612462586361", "0.42406544411364033", "0.4246715208825124", "0.4164467033566146", "0.43903009736054804", "0.41244812976278117", "0.41722285663131414", "0.42672824639720053", "0.4163123815318304", "0.4241854889819568"], 
  "stackgroup": None
}
trace4 = {
  "line": {"shape": "spline"}, 
  "meta": {"columnNames": {
      "x": "D", 
      "y": "A"
    }}, 
  "mode": "markers+lines", 
  "name": "200 ms", 
  "type": "scatter", 
  "x": ["25", "50", "75", "100", "125", "150", "175", "200", "225", "250", "275", "300", "325", "350", "375", "400", "425", "450", "475", "500"], 
  "y": ["0.668245194533538", "0.619880019050891", "0.5952759020992059", "0.5689752856268316", "0.5121187434126164", "0.5017092236295916", "0.5309873346096099", "0.5124555028790535", "0.5027443356735326", "0.5063825209183426", "0.5047606652452657", "0.48843349899638144", "0.49013988172966627", "0.4934775247276667", "0.4957390987177718", "0.48060527959998667", "0.4947328776128319", "0.5007738143102392", "0.5022764534022472", "0.48805706320375775"], 
  "visible": True, 
  "stackgroup": None
}
trace5 = {
  "line": {"shape": "spline"}, 
  "meta": {"columnNames": {
      "x": "D", 
      "y": "500 ms no-obs"
    }}, 
  "mode": "markers+lines", 
  "name": "500 ms", 
  "type": "scatter", 
  "x": ["500", "475", "450", "425", "400", "375", "350", "325", "300", "275", "250", "225", "200", "175", "150", "125", "100", "75", "50", "25"], 
  "y": ["0.664764123552645", "0.6700046374322083", "0.6782956666803572", "0.6732294348929854", "0.6848448565096656", "0.6674784248393044", "0.6753441836141788", "0.6825539796526395", "0.6895323534496607", "0.6939605088923563", "0.6953112227149412", "0.7045689948292818", "0.6883299555362765", "0.6880977188717633", "0.7010312027252428", "0.6792797263313097", "0.7327407083339247", "0.7562759384979947", "0.7696425583731311", "0.8183661513058429"], 
  "visible": True
}
data = [trace1, trace2, trace3, trace4, trace5]
layout = {
  #"title": {"text": "Click to enter Plot title"}, 
  "xaxis": {
    "type": "linear", 
    "range": [-1.543485793485786, 507.61590436590444],     
    "title": {"text": "Tx-Rx distance"}, 
    "domain": [0, 1], 
    "autorange": False,     
  }, 
  "yaxis": {
    "type": "linear", 
    "range": [-0.017505109611200664, 1.0222953763637457], 
    "title": {"text": "VAP"}, 
    "domain": [0, 1], 
    "autorange": False, 
    "showspikes": False
  }, 
  "legend": {
    "x": 0.34172749846624545, 
    "y": 0.9567358993902438, 
    "xanchor": "left", 
    "orientation": "h"
  }, 
  "autosize": True, 
  "dragmode": "zoom", 
  "template": {
    "data": {
      "bar": [
        {
          "type": "bar", 
          "marker": {"colorbar": {
              "ticks": "", 
              "outlinewidth": 0
            }}
        }
      ], 
      "table": [
        {
          "type": "table", 
          "cells": {
            "fill": {"color": "#EBF0F8"}, 
            "line": {"color": "white"}
          }, 
          "header": {
            "fill": {"color": "#C8D4E3"}, 
            "line": {"color": "white"}
          }
        }
      ], 
      "carpet": [
        {
          "type": "carpet", 
          "aaxis": {
            "gridcolor": "#C8D4E3", 
            "linecolor": "#C8D4E3", 
            "endlinecolor": "#2a3f5f", 
            "minorgridcolor": "#C8D4E3", 
            "startlinecolor": "#2a3f5f"
          }, 
          "baxis": {
            "gridcolor": "#C8D4E3", 
            "linecolor": "#C8D4E3", 
            "endlinecolor": "#2a3f5f", 
            "minorgridcolor": "#C8D4E3", 
            "startlinecolor": "#2a3f5f"
          }
        }
      ], 
      "mesh3d": [
        {
          "type": "mesh3d", 
          "colorbar": {
            "ticks": "", 
            "outlinewidth": 0
          }
        }
      ], 
      "contour": [
        {
          "type": "contour", 
          "colorbar": {
            "ticks": "", 
            "outlinewidth": 0
          }, 
          "autocolorscale": True
        }
      ], 
      "heatmap": [
        {
          "type": "heatmap", 
          "colorbar": {
            "ticks": "", 
            "outlinewidth": 0
          }, 
          "autocolorscale": True
        }
      ], 
      "scatter": [
        {
          "type": "scatter", 
          "marker": {"colorbar": {
              "ticks": "", 
              "outlinewidth": 0
            }}
        }
      ], 
      "surface": [
        {
          "type": "surface", 
          "colorbar": {
            "ticks": "", 
            "outlinewidth": 0
          }
        }
      ], 
      "heatmapgl": [
        {
          "type": "heatmapgl", 
          "colorbar": {
            "ticks": "", 
            "outlinewidth": 0
          }
        }
      ], 
      "histogram": [
        {
          "type": "histogram", 
          "marker": {"colorbar": {
              "ticks": "", 
              "outlinewidth": 0
            }}
        }
      ], 
      "parcoords": [
        {
          "line": {"colorbar": {
              "ticks": "", 
              "outlinewidth": 0
            }}, 
          "type": "parcoords"
        }
      ], 
      "scatter3d": [
        {
          "type": "scatter3d", 
          "marker": {"colorbar": {
              "ticks": "", 
              "outlinewidth": 0
            }}
        }
      ], 
      "scattergl": [
        {
          "type": "scattergl", 
          "marker": {"colorbar": {
              "ticks": "", 
              "outlinewidth": 0
            }}
        }
      ], 
      "choropleth": [
        {
          "type": "choropleth", 
          "colorbar": {
            "ticks": "", 
            "outlinewidth": 0
          }
        }
      ], 
      "scattergeo": [
        {
          "type": "scattergeo", 
          "marker": {"colorbar": {
              "ticks": "", 
              "outlinewidth": 0
            }}
        }
      ], 
      "histogram2d": [
        {
          "type": "histogram2d", 
          "colorbar": {
            "ticks": "", 
            "outlinewidth": 0
          }, 
          "autocolorscale": True
        }
      ], 
      "scatterpolar": [
        {
          "type": "scatterpolar", 
          "marker": {"colorbar": {
              "ticks": "", 
              "outlinewidth": 0
            }}
        }
      ], 
      "contourcarpet": [
        {
          "type": "contourcarpet", 
          "colorbar": {
            "ticks": "", 
            "outlinewidth": 0
          }
        }
      ], 
      "scattercarpet": [
        {
          "type": "scattercarpet", 
          "marker": {"colorbar": {
              "ticks": "", 
              "outlinewidth": 0
            }}
        }
      ], 
      "scattermapbox": [
        {
          "type": "scattermapbox", 
          "marker": {"colorbar": {
              "ticks": "", 
              "outlinewidth": 0
            }}
        }
      ], 
      "scatterpolargl": [
        {
          "type": "scatterpolargl", 
          "marker": {"colorbar": {
              "ticks": "", 
              "outlinewidth": 0
            }}
        }
      ], 
      "scatterternary": [
        {
          "type": "scatterternary", 
          "marker": {"colorbar": {
              "ticks": "", 
              "outlinewidth": 0
            }}
        }
      ], 
      "histogram2dcontour": [
        {
          "type": "histogram2dcontour", 
          "colorbar": {
            "ticks": "", 
            "outlinewidth": 0
          }, 
          "autocolorscale": True
        }
      ]
    }, 
    "layout": {
      "geo": {
        "bgcolor": "white", 
        "showland": True, 
        "lakecolor": "white", 
        "landcolor": "white", 
        "showlakes": True, 
        "subunitcolor": "#C8D4E3"
      }, 
      "font": {"color": "#2a3f5f", "size":18}, 
      "polar": {
        "bgcolor": "white", 
        "radialaxis": {
          "ticks": "", 
          "gridcolor": "#EBF0F8", 
          "linecolor": "#EBF0F8"
        }, 
        "angularaxis": {
          "ticks": "", 
          "gridcolor": "#EBF0F8", 
          "linecolor": "#EBF0F8"
        }
      }, 
      "scene": {
        "xaxis": {
          "ticks": "", 
          "gridcolor": "#DFE8F3", 
          "gridwidth": 2, 
          "linecolor": "#EBF0F8", 
          "zerolinecolor": "#EBF0F8", 
          "showbackground": True, 
          "backgroundcolor": "white"
        }, 
        "yaxis": {
          "ticks": "", 
          "gridcolor": "#DFE8F3", 
          "gridwidth": 2, 
          "linecolor": "#EBF0F8", 
          "zerolinecolor": "#EBF0F8", 
          "showbackground": True, 
          "backgroundcolor": "white"
        }, 
        "zaxis": {
          "ticks": "", 
          "gridcolor": "#DFE8F3", 
          "gridwidth": 2, 
          "linecolor": "#EBF0F8", 
          "zerolinecolor": "#EBF0F8", 
          "showbackground": True, 
          "backgroundcolor": "white"
        }
      }, 
      "title": {"x": 0.05}, 
      "xaxis": {
        "ticks": "", 
        "gridcolor": "#EBF0F8", 
        "linecolor": "#EBF0F8", 
        "automargin": True, 
        "zerolinecolor": "#EBF0F8", 
        "zerolinewidth": 2
      }, 
      "yaxis": {
        "ticks": "", 
        "gridcolor": "#EBF0F8", 
        "linecolor": "#EBF0F8", 
        "automargin": True, 
        "zerolinecolor": "#EBF0F8", 
        "zerolinewidth": 2
      }, 
      "ternary": {
        "aaxis": {
          "ticks": "", 
          "gridcolor": "#DFE8F3", 
          "linecolor": "#A2B1C6"
        }, 
        "baxis": {
          "ticks": "", 
          "gridcolor": "#DFE8F3", 
          "linecolor": "#A2B1C6"
        }, 
        "caxis": {
          "ticks": "", 
          "gridcolor": "#DFE8F3", 
          "linecolor": "#A2B1C6"
        }, 
        "bgcolor": "white"
      }, 
      "colorway": ["#636efa", "#EF553B", "#00cc96", "#ab63fa", "#19d3f3", "#e763fa", "#fecb52", "#ffa15a", "#ff6692", "#b6e880"], 
      "hovermode": "closest", 
      "colorscale": {
        "diverging": [
          [0, "#8e0152"], [0.1, "#c51b7d"], [0.2, "#de77ae"], [0.3, "#f1b6da"], [0.4, "#fde0ef"], [0.5, "#f7f7f7"], [0.6, "#e6f5d0"], [0.7, "#b8e186"], [0.8, "#7fbc41"], [0.9, "#4d9221"], [1, "#276419"]], 
        "sequential": [
          [0, "#0508b8"], [0.0893854748603352, "#1910d8"], [0.1787709497206704, "#3c19f0"], [0.2681564245810056, "#6b1cfb"], [0.3575418994413408, "#981cfd"], [0.44692737430167595, "#bf1cfd"], [0.5363128491620112, "#dd2bfd"], [0.6256983240223464, "#f246fe"], [0.7150837988826816, "#fc67fd"], [0.8044692737430168, "#fe88fc"], [0.8938547486033519, "#fea5fd"], [0.9832402234636871, "#febefe"], [1, "#fec3fe"]], 
        "sequentialminus": [
          [0, "#0508b8"], [0.0893854748603352, "#1910d8"], [0.1787709497206704, "#3c19f0"], [0.2681564245810056, "#6b1cfb"], [0.3575418994413408, "#981cfd"], [0.44692737430167595, "#bf1cfd"], [0.5363128491620112, "#dd2bfd"], [0.6256983240223464, "#f246fe"], [0.7150837988826816, "#fc67fd"], [0.8044692737430168, "#fe88fc"], [0.8938547486033519, "#fea5fd"], [0.9832402234636871, "#febefe"], [1, "#fec3fe"]]
      }, 
      "plot_bgcolor": "white", 
      "paper_bgcolor": "white", 
      "shapedefaults": {
        "line": {"width": 0}, 
        "opacity": 0.4, 
        "fillcolor": "#506784"
      }, 
      "annotationdefaults": {
        "arrowhead": 0, 
        "arrowcolor": "#506784", 
        "arrowwidth": 1
      }
    }, 
    #"themeRef": "PLOTLY_WHITE"
  }, 
  "showlegend": False
}

fig = Figure(data=data, layout=layout)
fig.write_image("images/AW_20Hz_2.pdf", format='pdf')

####### 10 HZ AW

trace1 = {
  "line": {"shape": "spline"}, 
  "meta": {"columnNames": {
      "x": "D", 
      "y": "A"
    }}, 
  "mode": "markers+lines", 
  "name": "10 ms", 
  "type": "scatter", 
  "x": ["25", "50", "75", "100", "125", "150", "175", "200", "225", "250", "275", "300", "325", "350", "375", "400", "425", "450", "475", "500"], 
  "y": ["0.06039542361690621", "0.0645282376295102", "0.05935849149591948", "0.05762238294381292", "0.05464052070646272", "0.054839110194933274", "0.05017668519258707", "0.053847552122863775", "0.05176903015473763", "0.05033783833503254", "0.051820729569750854", "0.05085564278068328", "0.050131900212839156", "0.05204047740130576", "0.05172711526732262", "0.05201949436820717", "0.05233556979034366", "0.05003808813653503", "0.05130631007881008", "0.04999120276708217"], 
  "visible": True, 
  "stackgroup": None
}
trace2 = {
  "line": {"shape": "spline"}, 
  "meta": {"columnNames": {
      "x": "D", 
      "y": "A"
    }}, 
  "mode": "markers+lines", 
  "name": "50 ms", 
  "type": "scatter", 
  "x": ["25", "50", "75", "100", "125", "150", "175", "200", "225", "250", "275", "300", "325", "350", "375", "400", "425", "450", "475", "500"], 
  "y": ["0.37492529855121903", "0.34390181139576653", "0.31432770578405567", "0.3009195326881855", "0.2811317799768976", "0.2913988865130947", "0.27096086891747045", "0.27503484489136654", "0.2790867480468753", "0.2763416732682553", "0.2733561703861952", "0.2770209405209611", "0.27815432001052737", "0.27311685528464724", "0.27456618109328046", "0.2705142527313615", "0.27890184248713823", "0.2859279529929919", "0.2729411975558091", "0.27486231481435"], 
  "visible": True, 
  "stackgroup": None
}
trace3 = {
  "line": {"shape": "spline"}, 
  "meta": {"columnNames": {
      "x": "D", 
      "y": "A"
    }}, 
  "mode": "markers+lines", 
  "name": "100 ms", 
  "type": "scatter", 
  "x": ["25", "50", "75", "100", "125", "150", "175", "200", "225", "250", "275", "300", "325", "350", "375", "400", "425", "450", "475", "500"], 
  "y": ["0.7024645067167219", "0.6682243583874053", "0.6538014916010753", "0.6024315611770257", "0.582170996444629", "0.5846582733990717", "0.5515861663458331", "0.5603996783645061", "0.5577595210386364", "0.5517724082895564", "0.5447570210472126", "0.5324736265223957", "0.562647219556772", "0.5554004007195961", "0.5204791340229471", "0.529796707133305", "0.5551916212233324", "0.5605212436137359", "0.5469319212920452", "0.5400411770002134"], 
  "stackgroup": None
}
trace4 = {
  "line": {"shape": "spline"}, 
  "meta": {"columnNames": {
      "x": "D", 
      "y": "A"
    }}, 
  "mode": "markers+lines", 
  "name": "200 ms", 
  "type": "scatter", 
  "x": ["25", "50", "75", "100", "125", "150", "175", "200", "225", "250", "275", "300", "325", "350", "375", "400", "425", "450", "475", "500"], 
  "y": ["0.7405088492331454", "0.7011323606862938", "0.6780056327979999", "0.6496261758452653", "0.6312546837524021", "0.6084012104742261", "0.5767131843342599", "0.616438687208754", "0.6002636398658502", "0.5880103618309619", "0.5986646881966863", "0.582070377337821", "0.6051734742767731", "0.584633865765287", "0.5898048212609815", "0.5727745192992884", "0.584893010352405", "0.570544582163727", "0.5624150837802481", "0.5799846249912748"], 
  "visible": True, 
  "stackgroup": None
}
trace5 = {
  "line": {"shape": "spline"}, 
  "meta": {"columnNames": {
      "x": "D", 
      "y": "500 ms no-obs"
    }}, 
  "mode": "markers+lines", 
  "name": "500 ms", 
  "type": "scatter", 
  "x": ["25", "50", "75", "100", "125", "150", "175", "200", "225", "250", "275", "300", "325", "350", "375", "400", "425", "450", "475", "500"], 
  "y": ["0.7671259626086976", "0.7790403534771297", "0.7589878430539551", "0.7208794103345751", "0.7009594103277945", "0.702147564028343", "0.6914130110789426", "0.6843677870670892", "0.673092707827009", "0.682803110759942", "0.6653137352113399", "0.6764370522820218", "0.6627427029152471", "0.6590424575863155", "0.674619139082608", "0.6719266080305187", "0.6759253323585975", "0.7045149803656131", "0.6696906380873491", "0.6707802772080168"], 
  "visible": True
}
data = Data([trace1, trace2, trace3, trace4, trace5])
layout = {
  "title": {"text": "Click to enter Plot title"}, 
  "xaxis": {
    "type": "linear", 
    "range": [-4.543485793485786, 510.61590436590444], 
    "ticks": "", 
    "title": {"text": "Tx-Rx distance"}, 
    "domain": [0, 1], 
    "autorange": False,    
  }, 
  "yaxis": {
    "type": "linear", 
    "range": [-0.017505109611200664, 1.0222953763637457], 
    "title": {"text": "VAP"}, 
    "domain": [0, 1], 
    "autorange": False, 
  }, 
  "legend": {
    "x": 0.34172749846624545, 
    "y": 0.9567358993902438, 
    "xanchor": "left", 
    "orientation": "h"
  }, 
  "autosize": True, 
  "dragmode": "zoom", 
  "template": {
    "data": {
      "bar": [
        {
          "type": "bar", 
          "marker": {"colorbar": {
              "ticks": "", 
              "outlinewidth": 0
            }}
        }
      ], 
      "table": [
        {
          "type": "table", 
          "cells": {
            "fill": {"color": "#EBF0F8"}, 
            "line": {"color": "white"}
          }, 
          "header": {
            "fill": {"color": "#C8D4E3"}, 
            "line": {"color": "white"}
          }
        }
      ], 
      "carpet": [
        {
          "type": "carpet", 
          "aaxis": {
            "gridcolor": "#C8D4E3", 
            "linecolor": "#C8D4E3", 
            "endlinecolor": "#2a3f5f", 
            "minorgridcolor": "#C8D4E3", 
            "startlinecolor": "#2a3f5f"
          }, 
          "baxis": {
            "gridcolor": "#C8D4E3", 
            "linecolor": "#C8D4E3", 
            "endlinecolor": "#2a3f5f", 
            "minorgridcolor": "#C8D4E3", 
            "startlinecolor": "#2a3f5f"
          }
        }
      ], 
      "mesh3d": [
        {
          "type": "mesh3d", 
          "colorbar": {
            "ticks": "", 
            "outlinewidth": 0
          }
        }
      ], 
      "contour": [
        {
          "type": "contour", 
          "colorbar": {
            "ticks": "", 
            "outlinewidth": 0
          }, 
          "autocolorscale": True
        }
      ], 
      "heatmap": [
        {
          "type": "heatmap", 
          "colorbar": {
            "ticks": "", 
            "outlinewidth": 0
          }, 
          "autocolorscale": True
        }
      ], 
      "scatter": [
        {
          "type": "scatter", 
          "marker": {"colorbar": {
              "ticks": "", 
              "outlinewidth": 0
            }}
        }
      ], 
      "surface": [
        {
          "type": "surface", 
          "colorbar": {
            "ticks": "", 
            "outlinewidth": 0
          }
        }
      ], 
      "heatmapgl": [
        {
          "type": "heatmapgl", 
          "colorbar": {
            "ticks": "", 
            "outlinewidth": 0
          }
        }
      ], 
      "histogram": [
        {
          "type": "histogram", 
          "marker": {"colorbar": {
              "ticks": "", 
              "outlinewidth": 0
            }}
        }
      ], 
      "parcoords": [
        {
          "line": {"colorbar": {
              "ticks": "", 
              "outlinewidth": 0
            }}, 
          "type": "parcoords"
        }
      ], 
      "scatter3d": [
        {
          "type": "scatter3d", 
          "marker": {"colorbar": {
              "ticks": "", 
              "outlinewidth": 0
            }}
        }
      ], 
      "scattergl": [
        {
          "type": "scattergl", 
          "marker": {"colorbar": {
              "ticks": "", 
              "outlinewidth": 0
            }}
        }
      ], 
      "choropleth": [
        {
          "type": "choropleth", 
          "colorbar": {
            "ticks": "", 
            "outlinewidth": 0
          }
        }
      ], 
      "scattergeo": [
        {
          "type": "scattergeo", 
          "marker": {"colorbar": {
              "ticks": "", 
              "outlinewidth": 0
            }}
        }
      ], 
      "histogram2d": [
        {
          "type": "histogram2d", 
          "colorbar": {
            "ticks": "", 
            "outlinewidth": 0
          }, 
          "autocolorscale": True
        }
      ], 
      "scatterpolar": [
        {
          "type": "scatterpolar", 
          "marker": {"colorbar": {
              "ticks": "", 
              "outlinewidth": 0
            }}
        }
      ], 
      "contourcarpet": [
        {
          "type": "contourcarpet", 
          "colorbar": {
            "ticks": "", 
            "outlinewidth": 0
          }
        }
      ], 
      "scattercarpet": [
        {
          "type": "scattercarpet", 
          "marker": {"colorbar": {
              "ticks": "", 
              "outlinewidth": 0
            }}
        }
      ], 
      "scattermapbox": [
        {
          "type": "scattermapbox", 
          "marker": {"colorbar": {
              "ticks": "", 
              "outlinewidth": 0
            }}
        }
      ], 
      "scatterpolargl": [
        {
          "type": "scatterpolargl", 
          "marker": {"colorbar": {
              "ticks": "", 
              "outlinewidth": 0
            }}
        }
      ], 
      "scatterternary": [
        {
          "type": "scatterternary", 
          "marker": {"colorbar": {
              "ticks": "", 
              "outlinewidth": 0
            }}
        }
      ], 
      "histogram2dcontour": [
        {
          "type": "histogram2dcontour", 
          "colorbar": {
            "ticks": "", 
            "outlinewidth": 0
          }, 
          "autocolorscale": True
        }
      ]
    }, 
    "layout": {
      "geo": {
        "bgcolor": "white", 
        "showland": True, 
        "lakecolor": "white", 
        "landcolor": "white", 
        "showlakes": True, 
        "subunitcolor": "#C8D4E3"
      }, 
      "font": {"color": "#2a3f5f", "size":18}, 
      "polar": {
        "bgcolor": "white", 
        "radialaxis": {
          "ticks": "", 
          "gridcolor": "#EBF0F8", 
          "linecolor": "#EBF0F8"
        }, 
        "angularaxis": {
          "ticks": "", 
          "gridcolor": "#EBF0F8", 
          "linecolor": "#EBF0F8"
        }
      }, 
      "scene": {
        "xaxis": {
          "ticks": "", 
          "gridcolor": "#DFE8F3", 
          "gridwidth": 2, 
          "linecolor": "#EBF0F8", 
          "zerolinecolor": "#EBF0F8", 
          "showbackground": True, 
          "backgroundcolor": "white"
        }, 
        "yaxis": {
          "ticks": "", 
          "gridcolor": "#DFE8F3", 
          "gridwidth": 2, 
          "linecolor": "#EBF0F8", 
          "zerolinecolor": "#EBF0F8", 
          "showbackground": True, 
          "backgroundcolor": "white"
        }, 
        "zaxis": {
          "ticks": "", 
          "gridcolor": "#DFE8F3", 
          "gridwidth": 2, 
          "linecolor": "#EBF0F8", 
          "zerolinecolor": "#EBF0F8", 
          "showbackground": True, 
          "backgroundcolor": "white"
        }
      }, 
      "title": {"x": 0.05}, 
      "xaxis": {
        "ticks": "", 
        "gridcolor": "#EBF0F8", 
        "linecolor": "#EBF0F8", 
        "automargin": True, 
        "zerolinecolor": "#EBF0F8", 
        "zerolinewidth": 2
      }, 
      "yaxis": {
        "ticks": "", 
        "gridcolor": "#EBF0F8", 
        "linecolor": "#EBF0F8", 
        "automargin": True, 
        "zerolinecolor": "#EBF0F8", 
        "zerolinewidth": 2
      }, 
      "ternary": {
        "aaxis": {
          "ticks": "", 
          "gridcolor": "#DFE8F3", 
          "linecolor": "#A2B1C6"
        }, 
        "baxis": {
          "ticks": "", 
          "gridcolor": "#DFE8F3", 
          "linecolor": "#A2B1C6"
        }, 
        "caxis": {
          "ticks": "", 
          "gridcolor": "#DFE8F3", 
          "linecolor": "#A2B1C6"
        }, 
        "bgcolor": "white"
      }, 
      "colorway": ["#636efa", "#EF553B", "#00cc96", "#ab63fa", "#19d3f3", "#e763fa", "#fecb52", "#ffa15a", "#ff6692", "#b6e880"], 
      "hovermode": "closest", 
      "colorscale": {
        "diverging": [
          [0, "#8e0152"], [0.1, "#c51b7d"], [0.2, "#de77ae"], [0.3, "#f1b6da"], [0.4, "#fde0ef"], [0.5, "#f7f7f7"], [0.6, "#e6f5d0"], [0.7, "#b8e186"], [0.8, "#7fbc41"], [0.9, "#4d9221"], [1, "#276419"]], 
        "sequential": [
          [0, "#0508b8"], [0.0893854748603352, "#1910d8"], [0.1787709497206704, "#3c19f0"], [0.2681564245810056, "#6b1cfb"], [0.3575418994413408, "#981cfd"], [0.44692737430167595, "#bf1cfd"], [0.5363128491620112, "#dd2bfd"], [0.6256983240223464, "#f246fe"], [0.7150837988826816, "#fc67fd"], [0.8044692737430168, "#fe88fc"], [0.8938547486033519, "#fea5fd"], [0.9832402234636871, "#febefe"], [1, "#fec3fe"]], 
        "sequentialminus": [
          [0, "#0508b8"], [0.0893854748603352, "#1910d8"], [0.1787709497206704, "#3c19f0"], [0.2681564245810056, "#6b1cfb"], [0.3575418994413408, "#981cfd"], [0.44692737430167595, "#bf1cfd"], [0.5363128491620112, "#dd2bfd"], [0.6256983240223464, "#f246fe"], [0.7150837988826816, "#fc67fd"], [0.8044692737430168, "#fe88fc"], [0.8938547486033519, "#fea5fd"], [0.9832402234636871, "#febefe"], [1, "#fec3fe"]]
      }, 
      "plot_bgcolor": "white", 
      "paper_bgcolor": "white", 
      "shapedefaults": {
        "line": {"width": 0}, 
        "opacity": 0.4, 
        "fillcolor": "#506784"
      }, 
      "annotationdefaults": {
        "arrowhead": 0, 
        "arrowcolor": "#506784", 
        "arrowwidth": 1
      }
    }, 
    #"themeRef": "PLOTLY_WHITE"
  }, 
  "showlegend": False
}

fig = Figure(data=data, layout=layout)
fig.write_image("images/AW_10Hz_2.pdf", format='pdf')