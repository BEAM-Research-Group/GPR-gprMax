def domain(x: float, y:  float, z: float):  # define domain size. x, y, z
    print('#domain: %.3f %.3f %.3f' % (x/39.37, y/39.37, z/39.37))


def discretization(dx: float, dy: float, dz: float):  # define discretization size. dx, dy, dz
    print('#dx_dy_dz: %.3f %.3f %.3f' % (dx/39.37, dy/39.37, dz/39.37))


def timewindow(a: str):  # enter as string
    print('#time_window:', a)


def addmat(relative_permittivity: float, conductivity: float, relative_permeability: float, magnetic_loss: float, name: str):  # Add materials and properties
    print('#material:', relative_permittivity, conductivity, relative_permeability, magnetic_loss, name)


def hertzian_source(wave_type: str, amplitude: float, center_frequency: float,  polarization: str, x_source: float, y_source: float, z_source: float):
    # source and waveform parameters
    print('#waveform:', wave_type, amplitude, center_frequency, 'my_wave')
    print('#hertzian_dipole:', polarization, '%.3f' % (x_source/39.37), '%.3f' % (y_source/39.37), '%.3f' % (z_source/39.37), 'my_wave')


def magnetic_source(wave_type: str, amplitude: float, center_frequency: float,  polarization: str, x_source: float, y_source: float, z_source: float):
    # source and waveform parameters
    print('#waveform:', wave_type, amplitude, center_frequency, 'my_wave')
    print('#magnetic_dipole:', polarization, x_source/39.37, y_source/39.37, z_source/39.37)


def receiver(x_receiver: float, y_receiver: float, z_receiver: float):  # receiver initial position
    print('#rx: %.3f %.3f %.3f' % (x_receiver/39.37, y_receiver/39.37, z_receiver/39.37))


def steps(x_step: float, y_step: float, z_step: float):  # for both source and receiver. No reason for difference
    print('#src_steps: %.3f %.3f %.3f' % (x_step/39.37, y_step/39.37, z_step/39.37))
    print('#rx_steps: %.3f %.3f %.3f' % (x_step/39.37, y_step/39.37, z_step/39.37))


def box1(x0: float, y0: float, z0: float, x_dim: float, y_dim: float, z_dim: float, material: str):  # bottom left back x, y, z & x, y, z dimensions
    print('#box: %.3f %.3f %.3f %.3f %.3f %.3f %s' % (x0/39.37, y0/39.37, z0/39.37, (x0+x_dim)/39.37, (y0+y_dim)/39.37, (z0+z_dim)/39.37, material))


def box2(x0: float, y0: float, z0: float, x1: float, y1: float, z1: float, material: str):  # bottom left back x, y, z & top right front x, y, z
    print('#box: %.3f %.3f %.3f %.3f %.3f %.3f %s' % (x0/39.37, y0/39.37, z0/39.37, x1/39.37, y1/39.37, z1/39.37, material))


def y_cylinder(x_base: float, y_base: float, z_base: float, height: float, radius: float, material: str):
    print('#cylinder: %.3f %.3f %.3f %.3f %.3f %.3f %.3f %s' % (x_base/39.37, y_base/39.37, z_base/39.37, x_base/39.37, (y_base+height)/39.37, z_base/39.37, radius/39.37, material))


domain(45.875,  100, 12)

discretization(3*0.03937, 3*0.03937, 3*0.03937)

timewindow('3e-9')

addmat(10, 0, 1, 50, 'testconc')
addmat(1, 10.1, 1, 0, 'testmetal')

hertzian_source('ricker', 1, 1.5*(10**9), 'y', 0.93388, 48, 7.625)
receiver(2.4748, 48, 7.625)

steps(0.15748, 0, 0)

box1(0,0,0,45.875,100,7.625,'testconc')

for x in range(11):
    box1(2.625+(3.75*x),0,1.25,2.75,100,5.125,'free_space')

for y in range(12):
    box1(1.25,11.75+(y*8),2.75,44.625,0.25,2,'testmetal')


for x in range(6):
    y_cylinder(3+(x*7.5),0,3.75,100,0.125,'testmetal')

for x in range(5):
    y_cylinder(6.75+(x*7.5),0,4.25,100,0.125,'testmetal')
