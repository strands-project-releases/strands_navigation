Name:           ros-hydro-topological-navigation
Version:        0.0.2
Release:        0%{?dist}
Summary:        ROS topological_navigation package

Group:          Development/Libraries
License:        MIT
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-hydro-actionlib
Requires:       ros-hydro-actionlib-msgs
Requires:       ros-hydro-geometry-msgs
Requires:       ros-hydro-message-runtime
Requires:       ros-hydro-mongodb-store
Requires:       ros-hydro-nav-msgs
Requires:       ros-hydro-rospy
Requires:       ros-hydro-scitos-msgs
Requires:       ros-hydro-sensor-msgs
Requires:       ros-hydro-std-msgs
Requires:       ros-hydro-strands-navigation-msgs
BuildRequires:  ros-hydro-actionlib
BuildRequires:  ros-hydro-actionlib-msgs
BuildRequires:  ros-hydro-catkin
BuildRequires:  ros-hydro-geometry-msgs
BuildRequires:  ros-hydro-message-generation
BuildRequires:  ros-hydro-nav-msgs
BuildRequires:  ros-hydro-rospy
BuildRequires:  ros-hydro-scitos-msgs
BuildRequires:  ros-hydro-sensor-msgs
BuildRequires:  ros-hydro-std-msgs
BuildRequires:  ros-hydro-strands-navigation-msgs

%description
The topological_navigation package

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/hydro/setup.sh" ]; then . "/opt/ros/hydro/setup.sh"; fi
mkdir -p build && cd build
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/hydro" \
        -DCMAKE_PREFIX_PATH="/opt/ros/hydro" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/hydro/setup.sh" ]; then . "/opt/ros/hydro/setup.sh"; fi
cd build
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/hydro

%changelog
* Wed Oct 29 2014 Jaime Pulido Fentanes <jpulidofentanes@lincoln.ac.uk> - 0.0.2-0
- Autogenerated by Bloom

