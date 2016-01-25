# Copyright 2016 Google Inc.
#
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.
# The Adobe DNG SDK, an API for reading and writing DNG files.
{
'targets': [{
  'target_name': 'dng_sdk-selector',
  'type': 'none',
  'conditions': [
    [ 'skia_android_framework', {
        'dependencies': [ 'android_deps.gyp:dng_sdk' ],
        'export_dependent_settings': [ 'android_deps.gyp:dng_sdk' ],
      }, {
        'dependencies': [ 'dng_sdk' ],
        'export_dependent_settings': [ 'dng_sdk' ],
    }]
  ]
},{
  'target_name': 'dng_sdk',
  'type': 'static_library',
  'cflags_cc': [ '-fexceptions' ],
  'cflags': [
    '-fexceptions',
    '-w',
  ],
  'msvs_settings': {
    'VCCLCompilerTool': {
      'WarningLevel': '0',
    },
  },
  'xcode_settings': {
    'WARNING_CFLAGS': ['-w'],
  },
  'dependencies': [
    'dng_dont_report_errors_flags',
    'dng_flags',
    'dng_frame_larger_than_flags',
    'dng_srcs',
    'linux_flags',
  ],
  'direct_dependent_settings': {
    'include_dirs': [
      '../third_party/externals/dng_sdk/source',
    ],
  },
}, {
  'target_name': 'dng_srcs',
  'type': 'none',
  'variables': {
    'headers': [
      '../third_party/externals/dng_sdk/source/RawEnvironment.h',
      '../third_party/externals/dng_sdk/source/dng_1d_function.h',
      '../third_party/externals/dng_sdk/source/dng_1d_table.h',
      '../third_party/externals/dng_sdk/source/dng_abort_sniffer.h',
      '../third_party/externals/dng_sdk/source/dng_area_task.h',
      '../third_party/externals/dng_sdk/source/dng_assertions.h',
      '../third_party/externals/dng_sdk/source/dng_auto_ptr.h',
      '../third_party/externals/dng_sdk/source/dng_bad_pixels.h',
      '../third_party/externals/dng_sdk/source/dng_bottlenecks.h',
      '../third_party/externals/dng_sdk/source/dng_camera_profile.h',
      '../third_party/externals/dng_sdk/source/dng_classes.h',
      '../third_party/externals/dng_sdk/source/dng_color_space.h',
      '../third_party/externals/dng_sdk/source/dng_color_spec.h',
      '../third_party/externals/dng_sdk/source/dng_date_time.h',
      '../third_party/externals/dng_sdk/source/dng_errors.h',
      '../third_party/externals/dng_sdk/source/dng_exceptions.h',
      '../third_party/externals/dng_sdk/source/dng_exif.h',
      '../third_party/externals/dng_sdk/source/dng_fast_module.h',
      '../third_party/externals/dng_sdk/source/dng_file_stream.h',
      '../third_party/externals/dng_sdk/source/dng_filter_task.h',
      '../third_party/externals/dng_sdk/source/dng_fingerprint.h',
      '../third_party/externals/dng_sdk/source/dng_flags.h',
      '../third_party/externals/dng_sdk/source/dng_gain_map.h',
      '../third_party/externals/dng_sdk/source/dng_globals.h',
      '../third_party/externals/dng_sdk/source/dng_host.h',
      '../third_party/externals/dng_sdk/source/dng_hue_sat_map.h',
      '../third_party/externals/dng_sdk/source/dng_ifd.h',
      '../third_party/externals/dng_sdk/source/dng_image.h',
      '../third_party/externals/dng_sdk/source/dng_image_writer.h',
      '../third_party/externals/dng_sdk/source/dng_info.h',
      '../third_party/externals/dng_sdk/source/dng_iptc.h',
      '../third_party/externals/dng_sdk/source/dng_jpeg_image.h',
      '../third_party/externals/dng_sdk/source/dng_lens_correction.h',
      '../third_party/externals/dng_sdk/source/dng_linearization_info.h',
      '../third_party/externals/dng_sdk/source/dng_lossless_jpeg.h',
      '../third_party/externals/dng_sdk/source/dng_matrix.h',
      '../third_party/externals/dng_sdk/source/dng_memory.h',
      '../third_party/externals/dng_sdk/source/dng_memory_stream.h',
      '../third_party/externals/dng_sdk/source/dng_misc_opcodes.h',
      '../third_party/externals/dng_sdk/source/dng_mosaic_info.h',
      '../third_party/externals/dng_sdk/source/dng_mutex.h',
      '../third_party/externals/dng_sdk/source/dng_negative.h',
      '../third_party/externals/dng_sdk/source/dng_opcode_list.h',
      '../third_party/externals/dng_sdk/source/dng_opcodes.h',
      '../third_party/externals/dng_sdk/source/dng_orientation.h',
      '../third_party/externals/dng_sdk/source/dng_parse_utils.h',
      '../third_party/externals/dng_sdk/source/dng_pixel_buffer.h',
      '../third_party/externals/dng_sdk/source/dng_point.h',
      '../third_party/externals/dng_sdk/source/dng_preview.h',
      '../third_party/externals/dng_sdk/source/dng_pthread.h',
      '../third_party/externals/dng_sdk/source/dng_rational.h',
      '../third_party/externals/dng_sdk/source/dng_read_image.h',
      '../third_party/externals/dng_sdk/source/dng_rect.h',
      '../third_party/externals/dng_sdk/source/dng_ref_counted_block.h',
      '../third_party/externals/dng_sdk/source/dng_reference.h',
      '../third_party/externals/dng_sdk/source/dng_render.h',
      '../third_party/externals/dng_sdk/source/dng_resample.h',
      '../third_party/externals/dng_sdk/source/dng_sdk_limits.h',
      '../third_party/externals/dng_sdk/source/dng_shared.h',
      '../third_party/externals/dng_sdk/source/dng_simple_image.h',
      '../third_party/externals/dng_sdk/source/dng_spline.h',
      '../third_party/externals/dng_sdk/source/dng_stream.h',
      '../third_party/externals/dng_sdk/source/dng_string.h',
      '../third_party/externals/dng_sdk/source/dng_string_list.h',
      '../third_party/externals/dng_sdk/source/dng_tag_codes.h',
      '../third_party/externals/dng_sdk/source/dng_tag_types.h',
      '../third_party/externals/dng_sdk/source/dng_tag_values.h',
      '../third_party/externals/dng_sdk/source/dng_temperature.h',
      '../third_party/externals/dng_sdk/source/dng_tile_iterator.h',
      '../third_party/externals/dng_sdk/source/dng_tone_curve.h',
      '../third_party/externals/dng_sdk/source/dng_types.h',
      '../third_party/externals/dng_sdk/source/dng_uncopyable.h',
      '../third_party/externals/dng_sdk/source/dng_utils.h',
      '../third_party/externals/dng_sdk/source/dng_xy_coord.h',
      '../third_party/externals/dng_sdk/source/dng_jpeg_memory_source.h',
      '../third_party/externals/dng_sdk/source/dng_jpeglib.h',
      '../third_party/externals/dng_sdk/source/dng_safe_arithmetic.h',
    ],
  },
  'dependencies': [
    'libjpeg-turbo.gyp:libjpeg-turbo',
    'zlib.gyp:zlib',
  ],
  'export_dependent_settings': [
    'libjpeg-turbo.gyp:libjpeg-turbo',
    'zlib.gyp:zlib',
  ],
  'direct_dependent_settings': {
    'sources': [
      '../third_party/externals/dng_sdk/source/dng_1d_function.cpp',
      '../third_party/externals/dng_sdk/source/dng_1d_table.cpp',
      '../third_party/externals/dng_sdk/source/dng_abort_sniffer.cpp',
      '../third_party/externals/dng_sdk/source/dng_area_task.cpp',
      '../third_party/externals/dng_sdk/source/dng_bad_pixels.cpp',
      '../third_party/externals/dng_sdk/source/dng_bottlenecks.cpp',
      '../third_party/externals/dng_sdk/source/dng_camera_profile.cpp',
      '../third_party/externals/dng_sdk/source/dng_color_space.cpp',
      '../third_party/externals/dng_sdk/source/dng_color_spec.cpp',
      '../third_party/externals/dng_sdk/source/dng_date_time.cpp',
      '../third_party/externals/dng_sdk/source/dng_exceptions.cpp',
      '../third_party/externals/dng_sdk/source/dng_exif.cpp',
      '../third_party/externals/dng_sdk/source/dng_file_stream.cpp',
      '../third_party/externals/dng_sdk/source/dng_filter_task.cpp',
      '../third_party/externals/dng_sdk/source/dng_fingerprint.cpp',
      '../third_party/externals/dng_sdk/source/dng_gain_map.cpp',
      '../third_party/externals/dng_sdk/source/dng_globals.cpp',
      '../third_party/externals/dng_sdk/source/dng_host.cpp',
      '../third_party/externals/dng_sdk/source/dng_hue_sat_map.cpp',
      '../third_party/externals/dng_sdk/source/dng_ifd.cpp',
      '../third_party/externals/dng_sdk/source/dng_image.cpp',
      '../third_party/externals/dng_sdk/source/dng_image_writer.cpp',
      '../third_party/externals/dng_sdk/source/dng_info.cpp',
      '../third_party/externals/dng_sdk/source/dng_iptc.cpp',
      '../third_party/externals/dng_sdk/source/dng_jpeg_image.cpp',
      '../third_party/externals/dng_sdk/source/dng_lens_correction.cpp',
      '../third_party/externals/dng_sdk/source/dng_linearization_info.cpp',
      '../third_party/externals/dng_sdk/source/dng_lossless_jpeg.cpp',
      '../third_party/externals/dng_sdk/source/dng_matrix.cpp',
      '../third_party/externals/dng_sdk/source/dng_memory.cpp',
      '../third_party/externals/dng_sdk/source/dng_memory_stream.cpp',
      '../third_party/externals/dng_sdk/source/dng_misc_opcodes.cpp',
      '../third_party/externals/dng_sdk/source/dng_mosaic_info.cpp',
      '../third_party/externals/dng_sdk/source/dng_mutex.cpp',
      '../third_party/externals/dng_sdk/source/dng_negative.cpp',
      '../third_party/externals/dng_sdk/source/dng_opcode_list.cpp',
      '../third_party/externals/dng_sdk/source/dng_opcodes.cpp',
      '../third_party/externals/dng_sdk/source/dng_orientation.cpp',
      '../third_party/externals/dng_sdk/source/dng_parse_utils.cpp',
      '../third_party/externals/dng_sdk/source/dng_pixel_buffer.cpp',
      '../third_party/externals/dng_sdk/source/dng_point.cpp',
      '../third_party/externals/dng_sdk/source/dng_preview.cpp',
      '../third_party/externals/dng_sdk/source/dng_pthread.cpp',
      '../third_party/externals/dng_sdk/source/dng_rational.cpp',
      '../third_party/externals/dng_sdk/source/dng_read_image.cpp',
      '../third_party/externals/dng_sdk/source/dng_rect.cpp',
      '../third_party/externals/dng_sdk/source/dng_ref_counted_block.cpp',
      '../third_party/externals/dng_sdk/source/dng_reference.cpp',
      '../third_party/externals/dng_sdk/source/dng_render.cpp',
      '../third_party/externals/dng_sdk/source/dng_resample.cpp',
      '../third_party/externals/dng_sdk/source/dng_shared.cpp',
      '../third_party/externals/dng_sdk/source/dng_simple_image.cpp',
      '../third_party/externals/dng_sdk/source/dng_spline.cpp',
      '../third_party/externals/dng_sdk/source/dng_stream.cpp',
      '../third_party/externals/dng_sdk/source/dng_string.cpp',
      '../third_party/externals/dng_sdk/source/dng_string_list.cpp',
      '../third_party/externals/dng_sdk/source/dng_tag_types.cpp',
      '../third_party/externals/dng_sdk/source/dng_temperature.cpp',
      '../third_party/externals/dng_sdk/source/dng_tile_iterator.cpp',
      '../third_party/externals/dng_sdk/source/dng_tone_curve.cpp',
      '../third_party/externals/dng_sdk/source/dng_utils.cpp',
      '../third_party/externals/dng_sdk/source/dng_xy_coord.cpp',
      '../third_party/externals/dng_sdk/source/dng_jpeg_memory_source.cpp',
      '../third_party/externals/dng_sdk/source/dng_safe_arithmetic.cpp',
    ],
    'include_dirs': [
      '../third_party/externals/dng_sdk/source',
      '../third_party/externals/libjpeg-turbo',
    ],
    'conditions': [
      ['skia_os != "linux"', {
        'sources': ['<@(headers)'],
      }],
    ],
  },
}, {
  'target_name': 'dng_flags',
  'type': 'none',
  'direct_dependent_settings': {
    'cflags_cc!': [ '-fno-rtti' ],
    'cflags': [
      '-DqDNGThreadSafe=1',
      '-DqDNGUseLibJPEG=1',
      '-DqDNGValidateTarget=1',
      '-DqDNGUseXMP=0',
      '-DqDNGBigEndian=0',
      '-w',
      '-fexceptions',
      '-frtti',
    ],
    'conditions': [
      ['skia_os == "ios" or skia_os == "mac"', {
        'xcode_settings': {
          'OTHER_CFLAGS': [
            '-DqDNGThreadSafe=1',
            '-DqDNGUseLibJPEG=1',
            '-DqDNGValidateTarget=1',
            '-DqDNGUseXMP=0',
            '-DqDNGBigEndian=0',
            '-w',
            '-fexceptions',
            '-frtti',
          ],
          'OTHER_CPLUSPLUSFLAGS': [
            '-DqDNGThreadSafe=1',
            '-DqDNGUseLibJPEG=1',
            '-DqDNGValidateTarget=1',
            '-DqDNGUseXMP=0',
            '-DqDNGBigEndian=0',
            '-w',
            '-fexceptions',
            '-frtti',
          ],
        },
      }],
    ],
  },
}, {
  'target_name': 'linux_flags',
  'type': 'none',
  'direct_dependent_settings': {
    'cflags': ['-DUNIX_ENV=1'],
  },
}, {
  'target_name': 'dng_dont_report_errors_flags',
  'type': 'none',
  'direct_dependent_settings': {
    'cflags': [
      '-DqDNGReportErrors=0',
      '-DqDNGValidate=0',
    ],
  },
}, {
  'target_name': 'dng_frame_larger_than_flags',
  'type': 'none',
  'direct_dependent_settings': {
    'cflags': ['-Wframe-larger-than=20000'],
  },
}],
}
