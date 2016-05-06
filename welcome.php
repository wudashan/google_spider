<?php
require_once('dbconn.php');
    $db = new dbconn();

	$sql = "select url from googleUrl where isvalid=1 order by rand() limit 1;";
	$url = $db->QueryOne($sql);
	echo $url;
	if ($url!='') {
		header("Location:{$url}");
	} else {
		header("Content-type: text/html; charset=utf-8");
		echo "<div style='margin:50px;font-size:15px;font-family: \"Microsoft YaHei\", 微软雅黑;'>不好意思，我的虫子暂时没有给您找到合适的地址，请稍后再试！</div>";
		#echo iconv("GB2312","UTF-8",'中文');
		#echo "<div style='margin:50px;font-size:15px;font-family: \"Microsoft YaHei\", 微软雅黑;'>不好意思，我的虫子暂时没有给您找到合适的地址，请稍后再试！</div>";
	}
?>