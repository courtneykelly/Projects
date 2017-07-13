'use strict';

console.log('Loading function');

exports.handler = (event, context, callback) => {
    var data = {"ip":event.context["source-ip"]};
    JSON.stringify(data);
    callback(null, data);  // Echo back the first key value
    //callback('Something went wrong');
};