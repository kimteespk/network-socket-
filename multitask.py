
import time
import threading

def toothbrush(brand):
    for i in range(10):
        print('brushing...ยาสีฟันยี่ห้อ ' + brand)  
        time.sleep(0.3)
    
def shower(soap, gel):
    for i in range(10):
        print('showering... สบู่{} ยาสระผม {}'.format(soap,gel))
        time.sleep(1)

task1 = threading.Thread(target=toothbrush, args=('colgage',))
task2 = threading.Thread(target=shower, args=('นกแก้ว', 'ซันซิ้ล'))

start = time.time()

#toothbrush()
#shower()

task1.start()
task2.start()
task1.join()
task2.join()


print('------------')
print('----------GO TO SCHOOL---------')
end = time.time()
print('Total time: ', end-start)