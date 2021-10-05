#!/usr/bin/env php
<?php

require_once 'vendor/autoload.php';

use App\Crud\Create;
use App\Crud\Delete;
use App\Crud\Read;
use App\Crud\Update;
use App\Helpers\DBHelper;
use App\Helpers\ListCommandsHelper;
use App\Helpers\ResponseHelper;
use App\Helpers\ValidatorsHelper;

//DBHelper::testConnection();

if (!isset($argv[1])) {
    echo "🚨 \e[91mIt's need passed a option\e[0m" . PHP_EOL;
    return;
}


switch ($argv[1]) {
    case '--create':
    case '-C':
        if (!ValidatorsHelper::verifyArgs($argv)) break;
        (new Create($argv))->handle();
        break;
    case '--read':
    case '-R':
        if (!ValidatorsHelper::verifyArgs($argv, 3)) break;
        (new Read($argv))->handle();
        break;
    case '--delete':
    case '-D':
        if (!ValidatorsHelper::verifyArgs($argv)) break;
        (new Delete($argv))->handle();
        break;
    case '--list' :
    case '-L':
        (new ListCommandsHelper())->getMessage();
        break;
//    case '--update':
//    case '-U':
//        (new Update($argv));
//        break;
    default:
        echo "🚨 \e[91mOption invalid\e[0m" . PHP_EOL;
}