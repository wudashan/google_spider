<?php
class dbconn {

    public $con;

    function __construct() {
        $con = mysql_connect("localhost","root","root");
	if (!$con) {
  	    die('Could not connect: ' . mysql_error());
  	}
	mysql_select_db("google_spider", $con);
    }

    function QueryOne($sql) {
        $result = mysql_query($sql);
	$row = mysql_fetch_array($result);
	return $row['url'];
    }
}
?>