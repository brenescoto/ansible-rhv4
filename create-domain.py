domain_name = 'sat_domain'
java_home = '/usr/java/jdk1.8.0_144'
middleware_home = '/home/admin/weblogic/WDLS/oracle_home'
#node_manager_home = '{{ nodemanager_home }}'
weblogic_home = '/home/admin/weblogic/WDLS/oracle_home/wlserver'
domain_configuration_home='/home/admin/weblogic/WDLS/domains/'+domain_name
weblogic_template=weblogic_home + '/common/templates/wls/wls.jar';
em_template=middleware_home + '/em/common/templates/wls/oracle.em_wls_template.jar';

readTemplate(weblogic_template);
setOption('DomainName', domain_name);
setOption('OverwriteDomain', 'true');
setOption('JavaHome', java_home);
setOption('ServerStartMode', 'prod');
cd('/Security/base_domain/User/weblogic');
cmo.setName('weblogic');
cmo.setUserPassword('welcome1');
cd('/');

print "SAVE DOMAIN";
writeDomain(domain_configuration_home);
closeTemplate();

updateDomain();
closeDomain();
