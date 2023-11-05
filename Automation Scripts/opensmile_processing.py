import os
import wave
from pydub import AudioSegment
import contextlib

import librosa
import soundfile as sf

import time


def get_wav_time(wav_path):
    '''
    Get audio file duration

         :param wav_path: audio path
         :return: audio duration (in seconds)
    '''
    x, _ = librosa.load(wav_path, sr=16000)
    sf.write('tmp.wav', x, 16000)
    with contextlib.closing(wave.open('tmp.wav', 'r')) as f:
        frames = f.getnframes()
    rate = f.getframerate()
    duration = frames / float(rate)
    return duration


def get_ms_part_wav(main_wav_path, start_time, end_time, part_wav_path):
    '''
         Audio slice, get part of the audio in millisecond level

         :param main_wav_path: original audio file path
         :param start_time: start time of interception
         :param end_time: the end time of the interception
         :param part_wav_path: audio path after interception
    :return:
    '''
    start_time = int(start_time)
    end_time = int(end_time)

    sound = AudioSegment.from_mp3(main_wav_path)
    word = sound[start_time:end_time]

    word.export(part_wav_path, format="wav")


def audio_folder_traversal(folder):

    print(f"<<< {folder} >>> traversal")
    for _ in range(22):
        if _ == 4 or _ == 10 or _ == 13 or _ == 14:
            print("Skipped S"+str(_+2)+"!")
            continue
        sub_folder = folder + 'S' + str(_ + 2) + '/'
        number_of_audio_files = 0
        count = 0
        for root, dir, files in os.walk(sub_folder):
            number_of_audio_files = len(files)
            if (int(input("Print files of " + sub_folder + " ? (1/0): "))):
                for i in range(number_of_audio_files):
                    print(files[i])
            print(sub_folder + " with " +
                  str(number_of_audio_files) + " files done !")
        if (int(input("Continue ? (1/0): "))):
            continue
        else:
            print("Breaking the loop to traverse other folders of " + path + "! Bye !")
            return


def audio_slicing(path, path_segment, slice_duration):

    print('Start cutting audio! ')
    # Duration of short audio after cutting in milliseconds
    time_segment = slice_duration
    for _ in range(22):

        if _ == 4 or _ == 10 or _ == 13 or _ == 14:
            print("Skipped S"+str(_+2)+"!")
            continue

        temp_path = path + 'S' + str(_ + 2) + '/'
        temp_path_segment = path_segment + 'S' + str(_ + 2) + '/'
        for root, dir, files in os.walk(temp_path):
            for i in range(len(files)):
                audio = root + files[i]
                # Convert to milliseconds
                time_all = int(get_wav_time(audio) * 1000)
                start_time = 0  # Start cutting from 0ms
                index = 1  # The serial number name after cutting, start the order from serial number 1
                while start_time <= time_all - time_segment:
                    print(str(files[i]) + ': ' + str(index))
                    end_time = start_time + time_segment
                    aduio_segment = temp_path_segment + \
                        files[i][:-4] + '_' + str(index) + '.wav'
                    get_ms_part_wav(audio, start_time, end_time, aduio_segment)
                    start_time += time_segment
                    index += 1
                # The next two lines are to cut out the audio that will eventually be less than time_segment duration
                aduio_segment = temp_path_segment + \
                    files[i][:-4] + '_' + str(index) + '.wav'
                get_ms_part_wav(audio, start_time, time_all, aduio_segment)
            if not (int(input("Continue ? (1/0): "))):
                return

    print('Audio cutting is complete! ')


def audio_processing(config_path, input_folder, output_folder):

    if (int(input("Firstly, do you want to list folder on terminal ? (1/0): "))):
        audio_folder_traversal(input_folder)

    print('Initiated processing audio! ')

    for _ in range(22):
        if _ == 4 or _ == 10 or _ == 13 or _ == 14:
            print("Skipped S"+str(_+2)+"!")
            continue
        input_sub_folder = input_folder + 'S' + str(_ + 2) + '/'
        output_sub_folder = output_folder + 'S' + str(_ + 2) + '/'
        print("##################################################")
        print("Folder :"+input_sub_folder)
        for root, dir, files in os.walk(input_sub_folder):
            count = 0
            number_of_audio_files = len(files)
            for i in range(number_of_audio_files):
                # path_remake(files[i])
                # time.sleep(2)
                print("----------------------------------------------")
                try:
                    input_file = files[i]
                    output_file = files[i][:-4] + '.arff'
                    print(f"<<<<<< {input_file} --->  {output_file} >>>>>>>")
                    os.system('SMILExtract -C ' + '\"' + config_path + '\"' + ' -I ' + '\"' + input_sub_folder +
                              input_file + '\"' + ' -O ' + output_sub_folder + output_file)
                except:
                    count += 1
            # Number of errors, no error occurs under normal circumstances.
            print(files[i] + ' errors: ' + str(count))


#####################################################
# One time run function to create folder structure
#####################################################
def folder_structure_creation(path):
    if not (int(input("Create folder structure in "+path+" ? (1/0): "))):
        print("Skipping folder structure creation !")
        return
    os.chdir(path)
    # os.system('cd '+path)
    for _ in range(22):
        if _ == 4 or _ == 10 or _ == 13 or _ == 14:
            print("Skipped S"+str(_+2)+"!")
            continue
        try:
            folder_name = 'S'+str(_+2)
            if (os.path.isdir(folder_name)):
                print("Skipped S"+str(_+2)+"! Folder already exists!")
                continue
            else:
                os.system('mkdir '+folder_name)
                print("S"+str(_+2)+" created !")
        except:
            print("Error in command")
    print("Folder structure created !")
    if (int(input("Continue ? (1/0): "))):
        return
    else:
        print("Stopping the code ! Bye !")
        exit()


if __name__ == '__main__':

    # Configuration file path
    config_path = r"C:/PROJECT/opensmile-3.0.1-win-x64/config/emobase/emobase.conf"
    # Original audio directory
    path = r"C:/PROJECT/Data/1.MONO/"
    # Audio directory after cutting
    sliced_audio_folder_path = r"C:/PROJECT/Data/2.MONO_sliced_audios/"
    # Folder with features after audio processing
    features_folder = r"C:/PROJECT/Data/3.MONO_sliced_audio_features_in_arff/"
    # Short audio duration in milliseconds
    short_audio_duration = 300

    folder_structure_creation(sliced_audio_folder_path)
    audio_slicing(path, sliced_audio_folder_path, short_audio_duration)
    # folder_structure_creation(features_folder)

    # audio_processing(config_path, sliced_audio_folder_path, features_folder)
