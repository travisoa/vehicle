def load():
	curb_weight = input('整备质量(kg):')
	saddle_weight = input('鞍载质量(kg):')
	wheelbase_4x2 = ['4200','3600']
	wheelbase_6x4 = ['3300','3825']
	wheelbase = input('轴距(mm):')
	saddle_f = input('鞍座前置距(mm):')
	saddle_f = int(saddle_f)
	if wheelbase in wheelbase_4x2:
		#saddle_f = 510
		weight_f = float(curb_weight)*0.65+float(saddle_weight)*saddle_f/int(wheelbase)
		weight_b = float(curb_weight)*0.35+float(saddle_weight)*(int(wheelbase)-saddle_f)/int(wheelbase)
	elif wheelbase in wheelbase_6x4:
		#saddle_f = 335
		weight_f = float(curb_weight)*0.55+float(saddle_weight)*saddle_f/(int(wheelbase)+1350/2)
		weight_b = float(curb_weight)*0.45+float(saddle_weight)*((int(wheelbase)+1350/2)-saddle_f)/(int(wheelbase)+1350/2)
	else:
		print('无此轴距,请重新输入')
		load()
	#weight_f = float(curb_weight)*0.65+float(saddle_weight)*saddle_f/int(wheelbase)
	#weight_b = float(curb_weight)*0.35+float(saddle_weight)*(int(wheelbase)-saddle_f)/int(wheelbase)
	print('前轴轴荷:' + str("%.2f" % weight_f) + 'kg;  ' + '后轴轴荷:' + str("%.2f" % weight_b) + 'kg;  ')
load()
