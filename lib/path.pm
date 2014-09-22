package path;

my %variables = (
    fop_current_version => "1.1",
    fop_current_version_release_date => "20 October 2012",
    fop_minimal_java_requirement => "1.6",
);


# taken from django's url.py

our @patterns = (
	[ qr!^/batik/.*\.mdtext$!, single_narrative => {
         header => "batik-top.html",
         sidenav => "batik-sidenav.mdtext",
         footer => "bottom.html",
         template => "single_narrative.html",
         preprocess => 1,
         %variables,
    } ],

	[ qr!^/fop/.*\.mdtext$!, single_narrative => {
         header => "fop-top.html",
         sidenav => "fop-sidenav.mdtext",
         footer => "bottom.html",
         template => "single_narrative.html",
         preprocess => 1,
         %variables,
    } ],

	[qr!\.mdtext$!, single_narrative => {
        header => "xgc-top.html",
        sidenav => "xgc-sidenav.mdtext",
        footer => "bottom.html",
        template => "single_narrative.html",
        preprocess => 1,
        %variables,
	} ],

	[qr!/sitemap\.html$!, sitemap => {
        headers => { title => "Sitemap" },
        sidenav => "xgc-sidenav.mdtext",
        footer  => "bottom.html",
        header  => "xgc-top.html",
    } ],
) ;

# for specifying interdependencies between files

our %dependencies = (
    "/sitemap.html" => [ grep s!^content!!, glob "content/*.mdtext" ],
);

1;

=head1 LICENSE

           Licensed to the Apache Software Foundation (ASF) under one
           or more contributor license agreements.  See the NOTICE file
           distributed with this work for additional information
           regarding copyright ownership.  The ASF licenses this file
           to you under the Apache License, Version 2.0 (the
           "License"); you may not use this file except in compliance
           with the License.  You may obtain a copy of the License at

             http://www.apache.org/licenses/LICENSE-2.0

           Unless required by applicable law or agreed to in writing,
           software distributed under the License is distributed on an
           "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
           KIND, either express or implied.  See the License for the
           specific language governing permissions and limitations
           under the License.

