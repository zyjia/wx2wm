/**
 * Created by Dzrea on 2016/12/5.
 */
 KindEditor.ready(function(K) {
            K.create('textarea[name=content]',{
                width:'800px',
                height:'200px',
                uploadJson:'/admin/upload/kindediter',
            });
        });