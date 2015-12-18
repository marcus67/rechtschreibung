#coding: utf-8
import spelling_mode

reload(spelling_mode)

def get_predefined_modes():
  
  modes = []
  
  mode = spelling_mode.spelling_mode()
  mode.name = u"Marcus Lieblingsregeln"
  mode.switch_simplification_c_kz = True
  mode.switch_simplification_ch_sch = True
  mode.switch_simplification_ck_kk = True
  mode.switch_simplification_th_t = True
  mode.switch_simplification_ph_f = True
  mode.switch_simplification_qu_kw = True
  mode.switch_simplification_v_fw = True
  mode.switch_simplification_x_ks = True
  mode.switch_simplification_y_uej = True
  mode.switch_simplification_sch_s = True
  mode.switch_simplification_tsch_c = True
  mode.switch_simplification_eu_oi = True
  mode.switch_simplification_ei_ai = True
  mode.switch_simplification_aumlu_oi = True
  mode.switch_simplification_ch_ck = True  
  mode.switch_simplification_suppress_mute_h = True
  mode.switch_simplification_d_t = True
  mode.segmented_control_harmonization_elongation = spelling_mode.ELONGATION_MODE_DOUBLE
  mode.switch_harmonization_homophony = True
  modes.append(mode)
  
  mode = spelling_mode.spelling_mode()
  mode.name = u"Vor Rechtschreibreform"
  mode.comment = "Rechtschreibregeln wie sie vor der Reform am XXXXX gültig waren."
  mode.isImmutable = True
  mode.switch_legacy_sz = True
  modes.append(mode)

  mode = spelling_mode.spelling_mode()
  mode.name = u"Aktuelle Rechtschreibung"
  mode.isImmutable = True
  mode.isReference = True
  modes.append(mode)

  return modes

