<?php
//Must declare aws stuff
require '../power/aws.phar';
      $sdk = new Aws\Sdk([
    'region'   => 'eu-west-1',
    'version'  => 'latest'
]);
$table = 'Pages';
//
$pageId = $_GET['id'];
echo "<div style='display:none;' class='pageId'>".$pageId."</div>"
//
//
//   try {
//
//   $response = $dynamodb->getItem ([
//     'TableName' => $table,
//     'ConsistentRead' => true,
//     'Key' => [
//         'string' => [
//             'S' => $parsedStringNoSpaces
//         ]
//     ]
// ] );
//
// //print $parsedString;
//   }//End of Try
//
// catch (Exception $e) {
//     echo 'Caught exception: ',  $e->getMessage(), "\n";
// }//End of catch

 ?>
