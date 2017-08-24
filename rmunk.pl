#!/usr/bin/perl

use strict;

my $wordlist = shift;
my $textfile = shift;

open FP, $wordlist or die "Cannot open word list $wordlist\n";
my %dict = ();
while( <FP> ) {
        my @a = split;
        $dict{$a[0]} = $a[1];
}
close FP;

open FP, $textfile or die "Cannot open text file $textfile\n";
while( <FP> ) {
        my @a = split;
        foreach my $w ( @a ) {
                my $outw = "<unk>";
                if( exists $dict{$w} ) {
                        $outw = $w;
                }
                print "$outw ";
        }
        print "\n";
}
close FP;

