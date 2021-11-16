prd = "HDNORIEGA/20211210asd@sadebd-cluster.gcba.gob.ar:1521/sadeprd.gcba.gob.ar"
SOLR_CORE_EE = "http://core-ee.gcba.gob.ar/solr/core-ee"
SOLR_CORE_GEDO = "http://core-gedo.gcba.gob.ar/solr/core-gedo"

datos = {
	"prd": "HDNORIEGA/20211210asd@sadebd-cluster.gcba.gob.ar:1521/sadeprd.gcba.gob.ar",
	"hml": "HDNORIEGA/13735457@sadebd-cluster.hml.gcba.gob.ar:1521/sadehml.hml.gcba.gob.ar",
	"standby":"HDNORIEGA/S2oxFnyj@dm01db01-vip.gcba.gob.ar:1521/sadetst.gcba.gob.ar",
	"stbsqlplus":"HDNORIEGA/20211210asd@(DESCRIPTION=(ADDRESS=(PROTOCOL=TCP)(Host=dm01db01-vip.gcba.gob.ar)(Port=1521))(CONNECT_DATA=(SERVICE_NAME=sadetst.gcba.gob.ar)))",
	"prdsqlplus":"HDNORIEGA/20211210asd@(DESCRIPTION=(ADDRESS=(PROTOCOL=TCP)(Host=sadebd-cluster.gcba.gob.ar)(Port=1521))(CONNECT_DATA=(SERVICE_NAME=sadeprd.gcba.gob.ar)))",
	"qa": "jbottarelli/JbO_gob19@exadb.gcba.gob.ar:1521/sadeqa.gcba.gob.ar"
}