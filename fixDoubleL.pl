#!/usr/bin/perl

use strict;
use warnings;
use 5.18.0;

# Usage:  
    # 1st Argument: The file to clean

print STDOUT "Run at " . localtime() . "\n\n";

my $input_file = $ARGV[0];
my $input_file_out = $input_file =~ s/\.txt/_clean.txt/gr;
my $i = 0;
open (FH, '<', $input_file) or die "Can't open input file '$input_file': $!";
open (FHOUT, '>', $input_file_out) or die "Can't open output file '$input_file_out': $!";

print STDOUT "Using '$input_file'\n";
print STDOUT "Output to '$input_file_out'\n\n";

my %replace = (
    "cal ed" => "called",
    "cal er" => "caller",
    "cal ing" => "calling",
    "cel ar" => "cellar",
    "col ar" => "collar",
    "col ude" => "collude",
    "col uding" => "colluding",
    "control ed" => "controlled",
    "fil ed" => "filled",
    "final y" => "finally",
    "fol owed" => "followed",
    "fol owing" => "following",
    "gueril a" => "",
    "hal oween" => "halloween",
    "hel o" => "hello",
    "hol ow" => "hollow",
    "il ness" => "illness",
    "mel ow" => "mellow",
    "metal ic" => "metallic",
    "pil ar" => "pillar",
    "pul ed" => "pulled",
    "real y" => "really",
    "smal er" => "smaller",
    "smel ed" => "smelled",
    "stil ness" => "stillness",
    "swal owed" => "swallowed",
    "swol en" => "swollen",
    "Versail es" => "Versailles",
    "vil a" => "villa",
    "wal et" => "wallet",
    "wal s" => "walls",
    "yel ow" => "yellow",
);

my $regex = join "|", map { quotemeta } sort { $b cmp $a } keys %replace;

$regex = qr/$regex/;

while (<FH>) {
    my $line = $_;

    $line =~ s/($regex)/$replace{$1}/g;

    print FHOUT $line; 

    $i++;

}

close FH or die "Can't close file: $_";
close FHOUT or die "Can't close file: $_";

print STDOUT "Cleaned $i words. \n";