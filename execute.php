<?php
        echo 'sudo -u mohan_akhil /home/mohan_akhil/instantpost.in/build.sh '.$_GET["repo"].'<br />';
        exec('python Handler_Server.py'.$_GET["repo"],
             $output, $return_code);
//        echo "Random Run: ".rand(101010, 999999)." Return Code: ".$return_code."<br />";
  //      foreach ($output as $id => $out)
    //        echo "Line ".($id + 1).": ".$out."<br />";
?>

